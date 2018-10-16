from os import environ
IPYTHONDIR = environ["IPYTHONDIR"]
template_rel_path = '~/Personal/ahsanijaz.github.io/_python'
template_path = IPYTHONDIR + template_rel_path
c.TemplateExporter.template_path = ['.',template_path]
