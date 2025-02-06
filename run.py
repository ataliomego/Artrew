import os
from app import create_app

# Membuat aplikasi dengan memanggil fungsi create_app() dari package app
app = create_app()

if __name__ == "__main__":
    # Menjalankan aplikasi Flask pada host 0.0.0.0 dan port yang didapatkan dari variabel lingkungan PORT
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
