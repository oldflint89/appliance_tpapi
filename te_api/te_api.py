from te_file_handler import TE
import os
import argparse


input_directory = "/home/admin/TE_API/input_files"
output_directory = "/home/admin/TE_API/te_response_data"
appliance_ip = "NNN.NNN.NNN.NNN"


def main():
    global input_directory
    global output_directory
    global appliance_ip
    parser = argparse.ArgumentParser()
    parser.add_argument("-id", "--input_directory", help="the input files folder to be scanned by TE")
    parser.add_argument("-od", "--output_directory", help="the output folder with TE results")
    parser.add_argument("-ip", "--appliance_ip", help="the appliance ip address")
    args = parser.parse_args()
    if args.input_directory:
        input_directory = args.input_directory
    print("The input files directory to be scanned by TE : {}".format(input_directory))
    if not os.path.exists(input_directory):
        print("The input files directory {} does not exist !".format(input_directory))
        return
    if args.output_directory:
        output_directory = args.output_directory
    print("The output directory with TE results : {}".format(output_directory))
    if not os.path.exists(output_directory):
        print("Pre-processing: creating te_api output directory {}".format(output_directory))
        try:
            os.mkdir(output_directory)
        except Exception as E1:
            print("could not create te_api output directory, because: {}".format(E1))
            raise
    if args.appliance_ip:
        appliance_ip = args.appliance_ip
    print("The appliance ip address : {}".format(appliance_ip))
    url = "https://" + appliance_ip + ":18194/tecloud/api/v1/file/"
    print("Handle input files")
    for file_name in os.listdir(input_directory):
        try:
            full_path = os.path.join(input_directory, file_name)
            print("Sending file: {} to TE".format(file_name))
            te = TE(url, file_name, full_path, output_directory)
            te.handle_file()
        except Exception as E:
            print("could not handle file: {} because: {}. will continue".format(file_name, E))
            continue


if __name__ == '__main__':
    main()