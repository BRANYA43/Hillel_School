def get_module_list_in_html_str(module_list: list) -> str:
    html_string = ''
    for i, module in enumerate(module_list):
        module = module.split("==")
        html_string += '<p>[{}] <i>{} {}</i>'.format(i + 1, module[0], module[1])
    return html_string
