from app import create_app

app = create_app()



if __name__ == '__main__':
    print('项目开始了')
    app.run(debug=app.config['DEBUG'])
