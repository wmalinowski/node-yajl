from os.path import abspath
import re
from sys import argv

def find_used_variables(text):
    variable_re = re.compile('\${([a-z_]+)}', re.MULTILINE | re.IGNORECASE)
    return variable_re.findall(text)

def find_variable_values(text, variables):
    values = {}
    for variable in variables:
        variable_re = re.compile('SET \(%s (.+)\)' % variable,
                               re.MULTILINE | re.IGNORECASE)
        values[variable] = variable_re.search(text).groups()[0]
    return values

def replace_variables(text, values):
    for key in values:
        text = text.replace('${%s}' % key, values[key])
    return text

def main(template_path, defines_path, output_path):
    with open(abspath(template_path), 'r') as template_file:
        template = template_file.read()
    variables = find_used_variables(template)

    with open(abspath(defines_path), 'r') as defines_file:
        defines = defines_file.read()
    values = find_variable_values(defines, variables)

    output = replace_variables(template, values)
    with open(abspath(output_path), 'w+') as output_file:
        output_file.write(output)

if __name__ == '__main__':
    main(argv[1], argv[2], argv[3])
