from flask import Flask, render_template, request

app = Flask(__name__)

books = [
    {"TITLE": "Kırmızı Pazartesi", "AUTHOR": "Gabriel Garcia Marquez"},
    {"TITLE": "Suç ve Ceza", "AUTHOR": "Fyodor Dostoyevski"},
    {"TITLE": "1984", "AUTHOR": "George Orwell"},
    {"TITLE": "Sineklerin Tanrısı", "AUTHOR": "William Golding"},
    {"TITLE": "Bülbülü Öldürmek", "AUTHOR": "Harper Lee"},
    {"TITLE": "Yeraltından Notlar", "AUTHOR": "Fyodor Dostoyevski"},
    {"TITLE": "Hayvan Çiftliği", "AUTHOR": "George Orwell"},
    {"TITLE": "Küçük Prens", "AUTHOR": "Antoine de Saint-Exupéry"},
    {"TITLE": "Harry Potter ve Felsefe Taşı", "AUTHOR": "J.K. Rowling"},
    {"TITLE": "Şeker Portakalı", "AUTHOR": "José Mauro de Vasconcelos"},
    {"TITLE": "İnce Memed I", "AUTHOR": "Yaşar Kemal"},
    {"TITLE": "İnce Memed II", "AUTHOR": "Yaşar Kemal"},
    {"TITLE": "İnce Memed III", "AUTHOR": "Yaşar Kemal"},
    {"TITLE": "Tutunamayanlar", "AUTHOR": "Oğuz Atay"},
    {"TITLE": "Saatleri Ayarlama Enstitüsü", "AUTHOR": "Ahmet Hamdi Tanpınar"},
    {"TITLE": "Kuyucaklı Yusuf", "AUTHOR": "Sabahattin Ali"},
    {"TITLE": "Aşk-ı Memnu", "AUTHOR": "Halit Ziya Uşaklıgil"},
    {"TITLE": "Beyaz Diş", "AUTHOR": "Jack London"},
    {"TITLE": "Monte Cristo Kontu", "AUTHOR": "Alexandre Dumas"},
    {"TITLE": "Notre Dame'ın Kamburu", "AUTHOR": "Victor Hugo"},
    {"TITLE": "Denizler Altında Yirmi Bin Fersah", "AUTHOR": "Jules Verne"},
    {"TITLE": "Dr. Jekyll ile Bay Hyde", "AUTHOR": "Robert Louis Stevenson"}
]


@app.route('/katalog')
def katalog():
    search_query = request.args.get('q', '')  # Arama kutusundan gelen değer
    filtered_books = []  # Boş liste ile başla
    
    if search_query:  # Kullanıcı arama yapmışsa filtrele
        filtered_books = [
            book for book in books 
            if search_query in book["TITLE"]
            or search_query in book["AUTHOR"]
        ]
    
    return render_template('katalog.html', data=filtered_books, query=search_query)

if __name__ == '__main__':
    app.run(debug=True)
