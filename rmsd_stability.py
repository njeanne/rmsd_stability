#!/usr/bin/env python3

"""
Created on 03 Feb. 2025
"""

__author__ = "Nicolas JEANNE"
__copyright__ = "GNU General Public License"
__email__ = "jeanne.n@chu-toulouse.fr"
__version__ = "1.0.0"

import argparse
import logging
import os
import re
import statistics
import sys

import pandas as pd


def create_log(path, level):
    """Create the log as a text file and as a stream.

    :param path: the path of the log.
    :type path: str
    :param level: the level og the log.
    :type level: str
    :return: the logging:
    :rtype: logging
    """

    log_level_dict = {"DEBUG": logging.DEBUG,
                      "INFO": logging.INFO,
                      "WARNING": logging.WARNING,
                      "ERROR": logging.ERROR,
                      "CRITICAL": logging.CRITICAL}

    if level is None:
        log_level = log_level_dict["INFO"]
    else:
        log_level = log_level_dict[level]

    if os.path.exists(path):
        os.remove(path)

    logging.basicConfig(format="%(asctime)s %(levelname)s:\t%(message)s",
                        datefmt="%Y/%m/%d %H:%M:%S",
                        level=log_level,
                        handlers=[logging.FileHandler(path), logging.StreamHandler()])
    return logging


if __name__ == "__main__":
    descr = f"""
    {os.path.basename(__file__)} v. {__version__}

    Created by {__author__}.
    Contact: {__email__}
    {__copyright__}

    Distributed on an "AS IS" basis without warranties or conditions of any kind, either express or implied.

    From the RMSD computation CSV files of the rms script (https://github.com/njeanne/rms), compute the mean and 
    standard deviation of the RMSD values from a start frame to an end frame.
    A CSV file of the RMSD means and standard deviations for the selection and for the whole data is produced.
    """
    parser = argparse.ArgumentParser(description=descr, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-o", "--out", required=True, type=str, help="the path to the output CSV file.")
    parser.add_argument("-s", "--start", required=False, default=1, type=int,
                        help="the start frame (1-index) to consider in the \"frames\" column. Default is one.")
    parser.add_argument("-e", "--end", required=False, type=int,
                        help="the end frame (1-index) to consider in the \"frames\" column. If not used the last frame "
                             "of the RMSD file is selected.")
    parser.add_argument("-l", "--log", required=False, type=str,
                        help="the path for the log file. If this option is skipped, the log file is created in the "
                             "output directory.")
    parser.add_argument("--log-level", required=False, type=str,
                        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
                        help="set the log level. If the option is skipped, log level is INFO.")
    parser.add_argument("--version", action="version", version=__version__)
    parser.add_argument("input", type=str, help="the path of the RMSD CSV file directory.")
    args = parser.parse_args()

    # create output directory if necessary
    output_directory = os.path.dirname(args.out)
    os.makedirs(output_directory, exist_ok=True)
    # create the logger
    if args.log:
        log_path = args.log
    else:
        log_path = os.path.join(output_directory, f"{os.path.splitext(os.path.basename(__file__))[0]}.log")
    create_log(log_path, args.log_level)

    logging.info(f"version: {__version__}")
    logging.info(f"CMD: {' '.join(sys.argv)}")
    if not args.end:
        logging.info(f"no --end option used, last frame will be selected.")
    
    data_stats = {"sample": [], "selected frames": [], "RMSD mean selected frames (\u212B)": [],
                  "RMSD standard deviation selected frames (\u212B)": [], "all frames": [],
                  "RMSD mean all frames (\u212B)": [],
                  "RMSD standard deviation all frames (\u212B)": []}
    pattern_sample = re.compile("RMSD_(.+)_ORF1.csv")

    for rmsd_csv in sorted(os.listdir(args.input)):
        df_rmsd = pd.read_csv(os.path.join(args.input, rmsd_csv), sep=",")
        last_frame = df_rmsd["frames"].iloc[-1] + 1
        if args.end:
            if args.end >= args.start:
                try:
                    raise argparse.ArgumentTypeError(f"--end {args.end} is greater or equal to --start {args.start}.")
                except argparse.ArgumentTypeError as ex:
                    logging.error(ex, exc_info=True)
                    sys.exit(1)
            try:
                if args.end > last_frame:
                    raise argparse.ArgumentTypeError(f"--end {args.end} is greater than the last frame of the input "
                                                     f"RMSD computation file for {rmsd_csv}: {last_frame}")
            except argparse.ArgumentTypeError as ex:
                logging.error(ex, exc_info=True)
                sys.exit(1)
            end = args.end
        else:
            end = last_frame

        # compute the stats for the whole data:
        sample = pattern_sample.match(rmsd_csv).group(1)
        if not sample:
            logging.error(f"the sample pattern \"{pattern_sample.pattern}\" do not match with the file {rmsd_csv}.")
            sys.exit(1)
        data_stats["sample"].append(sample)
        logging.info(f"{sample}:")
        all_frames = f"1 - {last_frame}"
        all_mean = round(statistics.mean(df_rmsd["RMSD"]), 2)
        all_standard_deviation = round(statistics.stdev(df_rmsd["RMSD"]), 2)
        data_stats["all frames"].append(all_frames)
        data_stats["RMSD mean all frames (\u212B)"].append(all_mean)
        data_stats["RMSD standard deviation all frames (\u212B)"].append(all_standard_deviation)
        logging.info(f"\tframes {all_frames}:")
        logging.info(f"\t\tRMSD mean:\t{all_mean} \u212B")
        logging.info(f"\t\tRMSD sd:\t{all_standard_deviation} \u212B")

        # compute the stats for the selection
        selection_frames = f"{args.start} - {end}"
        data_stats["selected frames"].append(selection_frames)
        idx_start = int(df_rmsd[df_rmsd["frames"] == args.start - 1].index[0])
        idx_end = int(df_rmsd[df_rmsd["frames"] == end - 1].index[0])
        subset = df_rmsd.iloc[idx_start:idx_end+1]
        selection_mean = round(statistics.mean(subset["RMSD"]), 2)
        selection_standard_deviation = round(statistics.stdev(subset["RMSD"]),2)
        data_stats["RMSD mean selected frames (\u212B)"].append(selection_mean)
        data_stats["RMSD standard deviation selected frames (\u212B)"].append(selection_standard_deviation)
        logging.info(f"\tframes {selection_frames}:")
        logging.info(f"\t\tRMSD mean:\t{selection_mean} \u212B")
        logging.info(f"\t\tRMSD sd:\t{selection_standard_deviation} \u212B")

    df_stats = pd.DataFrame.from_dict(data_stats)
    df_stats.to_csv(args.out, index=False, sep=";")
    logging.info(f"result file: {args.out}")
