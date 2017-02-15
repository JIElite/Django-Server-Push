import json
import csv

        
# for each word cloud for a topic
# The json data will be:
# {
#  "title": "your topic name",
#  "data" : [
#             {
#               "word": "cloud_word",
#               "weight: "weight_for_word_size"
#             },
#             ...
#             ...
#             ...
#            ]
# }
def __process_row_to_dict(row):
    if len(row) == 0:
        return None
    
    title = row[0]
    topic_cloud_dict = {
            "title": title,
            "data": [],
        }
    
    for word, weight in zip(row[1::2], row[2::2]):
        topic_cloud_dict["data"].append(
                {
                    "word": word,
                    "weight": weight,
                }
        )

    return topic_cloud_dict


# After retrieve data from csv
# The return looks like:
# [
#     {
#      "title": "your topic name",
#      "data" : [
#                 {
#                   "word": "cloud_word",
#                   "weight: "weight_for_word_size"
#                 },
#                 ...
#                 ...
#                 ...
#                ]
#     },
#     {
#      "title": "your topic name",
#      "data" : ...
#     },
#     ...
#     ...
#     ...
# ]
def __retrieve_data_from_csv(csv_filename):
    result_list = []
    with open(csv_filename) as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:

            topic_cloud_dict = __process_row_to_dict(row)
            if topic_cloud_dict is not None:
                result_list.append(topic_cloud_dict)
            else:
                pass
            
    return result_list


def transfer_topic_csv_to_jsonfile(
        csv_filename, output_json_filename,
        file_mode="w", indent=None, ensure_ascii=True):

    result_list = __retrieve_data_from_csv(csv_filename)      
    
    with open(output_json_filename, file_mode) as json_dump_file:
        json.dump(result_list, fp=json_dump_file, indent=indent, ensure_ascii=ensure_ascii)
    
    return


def transfer_topic_csv_to_json(csv_filename, indent=None, ensure_ascii=True):
    result_list = __retrieve_data_from_csv(csv_filename)
    return json.dumps(result_list, indent=indent, ensure_ascii=ensure_ascii)


def transfer_topic_csv_to_pyobj(csv_filename):
    result_list = __retrieve_data_from_csv(csv_filename)
    return result_list


# The following is demo code:
if __name__ == "__main__":
    # output to a file
    transfer_topic_csv_to_jsonfile("./data/LDA_Doc_dummyA.csv", "output.json", ensure_ascii=False, indent=2) 

    # get json obj
    json_obj = transfer_topic_csv_to_json("./data/LDA_Doc_dummyA.csv", ensure_ascii=False, indent=2)
    print(json_obj)
