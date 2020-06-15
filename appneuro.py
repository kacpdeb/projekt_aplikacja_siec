



































































































self.image.save(str(pathlib.Path(__file__).parent.absolute())+"/"+"epaint_obraz.png")
        image = cv2.imread("epaint_obraz.png")
        image = resize_image(image, 28, 28)
        cv2.imwrite("epaint_obraz.png",image)
        json_file = open('model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights("model.h5")
        img = imread('epaint_obraz.png')
        def rgb2gray(rgb):
            return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])
        gray = rgb2gray(img) 
        gray = gray.reshape((1, 28, 28, 1)) 
        prediction = loaded_model.predict(gray)
        QMessageBox.about(self, "Liczba to:", str(np.argmax(prediction)))