from wiki.singleton import SectionTree


def navbar_footer(request):
    section_tree = SectionTree().tree
    return {'section_tree': section_tree}
