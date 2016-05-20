import csv


class FileManager(object):
    FILE_PROCESS_FUNCTION = {
        "txt": "_get_links_from_txt",
        "csv": "_get_links_from_csv"
    }

    @staticmethod
    def _get_file_extension(path_file):
        return path_file.split(".")[-1]

    @classmethod
    def get_links(cls, path_file):
        file_extension = cls._get_file_extension(path_file)
        get_links_function = getattr(cls, cls.FILE_PROCESS_FUNCTION[file_extension])
        links = get_links_function(path_file)

        return links

    @staticmethod
    def _get_links_from_txt(path_file):
        with open(path_file, 'r') as txt_file:
            return {line for line in txt_file}

    @staticmethod
    def _get_links_from_csv(path_file):
        link_list = []
        with open(path_file, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',', quotechar='|')
            for row in reader:
                link_list.extend(row)
        return set(link_list)
