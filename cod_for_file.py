import os
class FileMaker():
    def make_merged_file(self):
        list_of_files = os.listdir('files')
        files_content = {}
        lines_count = []
        for file in list_of_files:
            f = open('files/' + file, "r")
            number_of_lines = 0
            lines = []
            for line in f:
                number_of_lines += 1
                lines.append(line)
            files_content[file] = {number_of_lines:  lines}
            lines_count.append(number_of_lines)
            f.close()
        result_file = open("result.txt", "w+")
        lines_count.sort()
        for number in lines_count:
            for file_name, content in files_content.items():
                for count, lines in content.items():
                    if number == count:
                        result_file.writelines(file_name)
                        result_file.writelines('\n')
                        result_file.writelines(str(count))
                        result_file.writelines('\n')
                        result_file.writelines(lines)
                        result_file.writelines('\n')
        result_file.close()
my_file_maker = FileMaker()
my_file_maker.make_merged_file()