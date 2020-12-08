# pip install flask
from flask import Flask, jsonify, make_response

app = Flask(__name__)

product_list = [
    {
        'id': 1,
        'img': 'https://gma.alicdn.com/bao/uploaded/i4/46562752/O1CN01boSkKv1WCSbZP6a29_!!0-saturn_solar.jpg',
        'product_uprice': 118,
        'product_price': 236,
        'desc': '小熊毛衣男韩版潮流宽松慵懒风港风日系复古保暖百搭ins冬季加厚'
    },
    {
        'id': 2,
        'img': 'https://gma.alicdn.com/bao/uploaded/i2/10807527/O1CN01Q3dzpl25TPosWOEoq_!!0-saturn_solar.jpg_400x400.jpg',
        'product_uprice': 118,
        'product_price': 489,
        'desc': '呈开美式纯色加厚窗帘遮光定制卧室客厅书房落地灰色隔热大气暮光',
    },
    {
        'id': 3,
        'img': 'https://img.alicdn.com/imgextra/i4/1980545515/TB2r2RUo3ZC2uNjSZFnXXaxZpXa_!!1980545515-0-beehive-scenes.jpg_360x360xzq90.jpg',
        'product_uprice': 245,
        'product_price': 268,
        'desc': 'LANCOME秋冬限量迷雾红管唇膏'
    },
    {
        'id': 4,
        'img': 'https://gma.alicdn.com/bao/uploaded/i4/54568379/O1CN01PEvwjY2BldH1reItP_!!0-saturn_solar.jpg_400x400.jpg',
        'product_uprice': 199,
        'product_price': 230,
        'desc': 'TIDEWORD大码男装高领毛衣男士纯色潮流保暖'
    },
    {
        'id': 5,
        'img': '//img.alicdn.com/bao/uploaded/i1/2210999090/TB2mfTjmTnI8KJjy0FfXXcdoVXa_!!2210999090.jpg_400x400q90.jpg',
        'product_uprice': 78,
        'product_price': 199,
        'desc': '韩版百搭套头可爱小狗图案宽松毛衣 男女情侣半高领打底针织衫潮'
    },
    {
        'id': 6,
        'img': 'https://gma.alicdn.com/bao/uploaded/i4/46562752/O1CN01boSkKv1WCSbZP6a29_!!0-saturn_solar.jpg',
        'product_uprice': 118,
        'product_price': 236,
        'desc': '小熊毛衣男韩版潮流宽松慵懒风港风日系复古保暖百搭ins冬季加厚'
    },
    {
        'id': 7,
        'img': 'https://gma.alicdn.com/bao/uploaded/i2/10807527/O1CN01Q3dzpl25TPosWOEoq_!!0-saturn_solar.jpg_400x400.jpg',
        'product_uprice': 118,
        'product_price': 489,
        'desc': '呈开美式纯色加厚窗帘遮光定制卧室客厅书房落地灰色隔热大气暮光',
    },
    {
        'id': 8,
        'img': 'https://img.alicdn.com/imgextra/i4/1980545515/TB2r2RUo3ZC2uNjSZFnXXaxZpXa_!!1980545515-0-beehive-scenes.jpg_360x360xzq90.jpg',
        'product_uprice': 245,
        'product_price': 268,
        'desc': 'LANCOME秋冬限量迷雾红管唇膏'
    },
    {
        'id': 9,
        'img': 'https://gma.alicdn.com/bao/uploaded/i4/54568379/O1CN01PEvwjY2BldH1reItP_!!0-saturn_solar.jpg_400x400.jpg',
        'product_uprice': 199,
        'product_price': 230,
        'desc': 'TIDEWORD大码男装高领毛衣男士纯色潮流保暖'
    },
    {
        'id': 10,
        'img': '//img.alicdn.com/bao/uploaded/i1/2210999090/TB2mfTjmTnI8KJjy0FfXXcdoVXa_!!2210999090.jpg_400x400q90.jpg',
        'product_uprice': 78,
        'product_price': 199,
        'desc': '韩版百搭套头可爱小狗图案宽松毛衣 男女情侣半高领打底针织衫潮'
    },
]

@app.route('/')
@app.route('/list')
def index():
    data = [
        {
            'id': list['id'],
            'img': list['img'],
            'product_uprice': list['product_uprice'],
            'product_price': list['product_price']
        }
        for list in product_list
    ]
    #  make_response解决跨域问题
    res = make_response(jsonify(data))
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Method'] = '*'
    res.headers['Access-Control-Allow-Headers'] = '*'

    return res

@app.route('/detail/<int:id>')
def detail(id):
    res = list(filter(lambda d: d['id']==id, product_list))
    data = res and res[0] and {
        'id': res[0]['id'], 
        'desc': res[0]['desc'],
        'img': res[0]['img']
    }
    #  make_response解决跨域问题
    res = make_response(jsonify(data))
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Method'] = '*'
    res.headers['Access-Control-Allow-Headers'] = '*'

    return res

if __name__ == "__main__":
    # app.config["JSON_AS_ASCII"] = False
    app.run(debug=True, port=8000)