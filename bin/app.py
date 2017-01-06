import web
from chemspipy import ChemSpider
cs = ChemSpider('47f53335-bd35-4d28-9074-d5fe9a69906a')

urls = (
  '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class Index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(equation="Hello")
        # also_left = [cs.search(x)[0].image_url.encode('ascii','ignore') for x in left]
        expressions = form.equation.split('->') # expressions is a list of expressions like (compound1 + compound2 + ...)
        compounds_expressions = [x.split('+') for x in expressions] # list of lists
        expression_compound_objects = [[cs.search(compound)[-1] for compound in expression] for expression in compounds_expressions]
        # chemical_expressions = [' + '.join(x) for x in molecular_formulas]
        # chem_eqn = r" \rightarrow ".join(chemical_expressions)

        chem_eqn_images = []
        for expression in expression_compound_objects:
            # chem_eqn_images.pop()
            for compound in expression:
                if is_organic(compound):
                    chem_eqn_images.append(compound.image_url.encode('ascii', 'ignore'))
                else:
                    chem_eqn_images.append("https://latex.codecogs.com/gif.latex?\dpi{200}" + compound.molecular_formula)
                chem_eqn_images.append("https://latex.codecogs.com/gif.latex?\dpi{200}+")
            chem_eqn_images.pop()
            chem_eqn_images.append(r"https://latex.codecogs.com/gif.latex?\dpi{200}\rightarrow")
        chem_eqn_images.pop()




        return render.index(equation = chem_eqn_images)


def is_organic(compound):
    SMILES_string = compound.smiles

    elements_with_c = ['Cd', 'Ca', 'Cf', 'Ce', 'Cs', 'Cl', 'Cr', 'Co', 'Cu', 'Cm']

    for x in elements_with_c:
        SMILES_string = SMILES_string.replace(x, "")

    if 'C' in SMILES_string or 'c' in SMILES_string:
        return True
    else:
        return False


if __name__ == "__main__":
    # benzene = cs.search("benzene")[-1]
    # toluene = cs.search("toluene")[-1]
    # alcl3 = cs.search("alcl3")[-1]
    # h2 = cs.search("h2")[-1]

    # print("benzene", is_organic(benzene))
    # print("toluene", is_organic(toluene))
    # print("alcl3", is_organic(alcl3))
    # print("h2", is_organic(h2))
    # print("chlorobenzene", is_organic(cs.search("chlorobenzene")[-1]))


    app.run()