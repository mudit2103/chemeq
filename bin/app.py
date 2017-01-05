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
        # compound1 = cs.search(form.equation)
        # compound2 = cs.search(form.name)

        two_halves = form.equation.split('->')
        string = two_halves
        left = two_halves[0]
        right = two_halves[1]

        left = left.split('+')
        right = right.split('+')

        left = [cs.search(x)[0].molecular_formula for x in left]
        right = [cs.search(x)[0].molecular_formula for x in right]


        left = ' + '.join(left)
        right = ' + '.join(right)
        string = left + r" \rightarrow " + right











        greeting = "%s" % (string)
        return render.index(equation = greeting)

if __name__ == "__main__":
    app.run()