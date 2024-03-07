from flask import Flask, render_template

app = Flask(__name__)

# Задание
#
# Создать базовый шаблон для интернет-магазина, содержащий общие
# элементы дизайна (шапка, меню, подвал), и дочерние шаблоны для
# страниц категорий товаров и отдельных товаров. Например, создать
# страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон..

@app.route('/')
def base():
    return render_template('base.html')


@app.route('/clothes/')
def clothes():
    return render_template('clothes.html')


@app.route('/shoes/')
def shoes():
    return render_template('shoes.html')


@app.route('/underwear/')
def underwear():
    return render_template('underwear.html')


if __name__ == '__main__':
    app.run(debug=True)
