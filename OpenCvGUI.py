import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import cv2
import numpy as np
from PIL import Image
from PIL import ImageTk


class Button:

    def __init__(self, root, frame3):
        self.root = root
        self.frame3 = frame3
        self.radio_var = tk.IntVar()
        self.path_selected = 'none'
        self.paths = []
        self.radio_handle = []
        self.check_value = []

    def on_click_select_button(self, fname_label):
        print('select button clicked')
        fileType = [('jpg/png file', ('*.jpg', '*.png'))]
        self.path_selected = filedialog.askopenfilename(filetypes=fileType)
        fname_label['text'] = os.path.basename(self.path_selected)

    def on_click_upload_button(self, path='None', image='None'):
        print('upload button clicked')

        if path == 'None':
            path = self.path_selected
        else:
            cv2.imwrite(path, image)

        if path in self.paths:
            messagebox.showerror('Upload Error', '"'
                                 + path
                                 + '"' + ' is already uploaded.')
        else:
            self.paths.append(path)
            self.create_radio_button(path)

    def on_click_show_button(self, method):
        global file_name
        print('showButton clicked')
        image = cv2.imread(self.paths[self.radio_var.get()])
        image = self.image_processing(image, method)

        file_name = os.path.basename(self.paths[self.radio_var.get()])
        name, ext = os.path.splitext(file_name)
        path = 'Data/images/' + name + '_' + method + ext

        # cv2.imwrite(path, image)
        self.open_image_window(path, image)

    def image_processing(self, image, method):
        if method == 'gray':
            image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        elif method == 'binary':
            ret2, image = cv2.threshold(image[:, :, 0], 0, 255, cv2.THRESH_OTSU)

        elif method == 'gblur':
            image = cv2.GaussianBlur(image, (9, 9), 0)

        elif method == 'canny':
            image = cv2.Canny(image, 100, 400)

        # elif method == 'Send_to_Directory':
        # image = os.mkdir("Differece_images")

        else:
            print('method is wrong')

        return image

    def create_radio_button(self, path):

        image = cv2.imread(path)
        # image = cv2.resize(image,(120,120))
        image = self.scale_to_height(image, 120)
        image_tk = self.to_tk_image(image)

        radio_button = tk.Radiobutton(self.frame3, image=image_tk,
                                      value=len(self.radio_handle),
                                      variable=self.radio_var)
        self.radio_var.set(0)
        self.radio_handle.append(radio_button)
        self.check_value.append(self.radio_var)

        radio_button.grid(row=(len(self.radio_handle) - 1) // 3,
                          column=(len(self.radio_handle) - 1) % 3)
        self.root.mainloop()

    def open_image_window(self, path, image):

        if image.shape[0] > 300:
            image = self.scale_to_height(image, 300)

        img_win = tk.Toplevel(self.root)
        fname = os.path.basename(path)
        img_win.title(fname)
        img_canvas = tk.Canvas(img_win, width=image.shape[1],
                               height=image.shape[0])
        img_canvas.pack()
        image_tk = self.to_tk_image(image)
        img_canvas.create_image(0, 0, image=image_tk, anchor='nw')

        uploadButton2 = tk.Button(img_win, text='upload',
                                  command=lambda: self.on_click_upload_button(path, image))
        uploadButton2.pack()

        self.root.mainloop()

    def to_tk_image(self, image_bgr):
        image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
        image_pil = Image.fromarray(image_rgb)
        image_tk = ImageTk.PhotoImage(image_pil)

        return image_tk

    def scale_to_height(self, img, height):
        scale = height / img.shape[0]
        return cv2.resize(img, dsize=None, fx=scale, fy=scale)


class Sample_Button(Button):

    def __init__(self, root, frame6):
        self.root = root
        self.frame6 = frame6
        self.Sample_radio_var = tk.IntVar()
        self.Sample_path_selected = 'none'
        self.Sample_paths = []
        self.Sample_radio_handle = []
        self.Sample_check_value = []

    def on_click_select_button_Sample(self, Sample_fname_label):
        print('select Sample button clicked')
        Sample_fileType = [('jpg/png file', ('*.jpg', '*.png'))]
        self.Sample_path_selected = filedialog.askopenfilename(filetypes=Sample_fileType)
        Sample_fname_label['text'] = os.path.basename(self.Sample_path_selected)

    def on_click_upload_button_Sample(self, Sample_path='None', Sample_image='None'):
        print('upload Sample button clicked')

        if Sample_path == 'None':
            Sample_path = self.Sample_path_selected
        else:
            cv2.imwrite(Sample_path, Sample_image)

        if Sample_path in self.Sample_paths:
            messagebox.showerror('Upload Error', '"'
                                 + Sample_path
                                 + '"' + ' Sample is already uploaded.')
        else:
            self.Sample_paths.append(Sample_path)
            self.create_Sample_radio_button(Sample_path)

    def on_click_show_button_Sample(self, Sample_method):
        global Sample_file_name

        print('show Sample Button clicked')
        Sample_image = cv2.imread(self.Sample_paths[self.Sample_radio_var.get()])
        Sample_image = self.Sample_image_processing(Sample_image, Sample_method)

        Sample_file_name = os.path.basename(self.Sample_paths[self.Sample_radio_var.get()])
        Sample_name, ext = os.path.splitext(Sample_file_name)
        Sample_path = 'Data/Sample_images/' + Sample_name + '_' + Sample_method + ext

        # cv2.imwrite(path, image)
        self.open_Sample_image_window(Sample_path, Sample_image)

    def Sample_image_processing(self, Sample_image, Sample_method):
        if Sample_method == 'Sample_gray':
            Sample_image = cv2.cvtColor(Sample_image, cv2.COLOR_RGB2GRAY)

        elif Sample_method == 'Sample_binary':
            Sample_ret2, Sample_image = cv2.threshold(Sample_image[:, :, 0], 0, 255, cv2.THRESH_OTSU)

        elif Sample_method == 'Sample_gblur':
            Sample_image = cv2.GaussianBlur(Sample_image, (9, 9), 0)

        elif Sample_method == 'Sample_canny':
            Sample_image = cv2.Canny(Sample_image, 100, 400)

        # elif Sample_method == 'Send_to_Directory':
        # Sample_image = os.mkdir("data/Sample_Differece_images")

        else:
            print('Sample method is wrong')

        return Sample_image

    def create_Sample_radio_button(self, Sample_path):

        Sample_image = cv2.imread(Sample_path)

        # image = cv2.resize(image,(120,120))
        Sample_image = self.scale_to_height_Sample(Sample_image, 120)
        Sample_image_tk = self.Sample_to_tk_image(Sample_image)

        Sample_radio_button = tk.Radiobutton(self.frame6, image=Sample_image_tk,
                                             value=len(self.Sample_radio_handle),
                                             variable=self.Sample_radio_var)
        self.Sample_radio_var.set(0)
        self.Sample_radio_handle.append(Sample_radio_button)
        self.Sample_check_value.append(self.Sample_radio_var)

        Sample_radio_button.grid(row=(len(self.Sample_radio_handle) - 1) // 3,
                                 column=(len(self.Sample_radio_handle) - 1) % 3)
        self.root.mainloop()

    def open_Sample_image_window(self, Sample_path, Sample_image):

        if Sample_image.shape[0] > 300:
            Sample_image = self.scale_to_height_Sample(Sample_image, 300)

        Sample_img_win = tk.Toplevel(self.root)
        Sample_fname = os.path.basename(Sample_path)
        Sample_img_win.title(Sample_fname)
        Sample_img_canvas = tk.Canvas(Sample_img_win, width=Sample_image.shape[1],
                                      height=Sample_image.shape[0])
        Sample_img_canvas.pack()
        Sample_image_tk = self.Sample_to_tk_image(Sample_image)
        Sample_img_canvas.create_image(0, 0, image=Sample_image_tk, anchor='nw')

        uploadSampleButton2 = tk.Button(Sample_img_win, text='Upload Sample',
                                        command=lambda: self.on_click_upload_button_Sample(Sample_path, Sample_image))
        uploadSampleButton2.pack()

        self.root.mainloop()

    def Sample_to_tk_image(self, Sample_image_bgr):
        Sample_image_rgb = cv2.cvtColor(Sample_image_bgr, cv2.COLOR_BGR2RGB)
        Sample_image_pil = Image.fromarray(Sample_image_rgb)
        Sample_image_tk = ImageTk.PhotoImage(Sample_image_pil)

        return Sample_image_tk

    def scale_to_height_Sample(self, Sample_img, height):
        scale = height / Sample_img.shape[0]
        return cv2.resize(Sample_img, dsize=None, fx=scale, fy=scale)


class Difference_Button(Sample_Button, Button):
    def on_click_diff_per_button(self, diff_per):

        threshold = 0.8
        resultsDirectory = 'Data/Differece_images'
        sourceDirectory = os.fsencode('Data/images')
        templateDirectory = os.fsencode('Data/Sample_images')
        detectedCount = 0

        for file in os.listdir(sourceDirectory):
            filename = os.fsdecode(file)
            if filename.endswith(".jpg") or filename.endswith(".png"):
                print(filename)
                img = cv2.imread('Data/images/' + filename)
                im_grayRef = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                for templateFile in os.listdir(templateDirectory):
                    templateFilename = os.fsdecode(templateFile)
                    print("_vs_" + templateFilename)
                    if filename.endswith(".jpg") or filename.endswith(".png"):
                        Sample_image = cv2.imread('Data/Sample_images/' + templateFilename, 0)
                        cv2.waitKey(0)
                        w, h = Sample_image.shape[::-1]
                        score = cv2.matchTemplate(im_grayRef, Sample_image, cv2.TM_CCOEFF_NORMED)
                        cv2.waitKey(0)
                        loc = np.where(score >= threshold)

                        if (len(loc[0])):
                            detectedCount = detectedCount + 1
                            for pt in zip(*loc[::-1]):
                                cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

                        if score * 100 > 70:
                            new_text = '{}_&_{} is Matched by {}'.format(filename, templateFilename, score * 100)
                        else:
                            cv2.imwrite(resultsDirectory + '/diff_per_' + filename + '.jpg', img)
                            new_text = '{}_&_{} Not Matched by {}'.format(filename, templateFilename, score * 100)
                        Difference_per_label["text"] += "\n" + new_text

                continue
            else:
                continue


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Image GUI')
    root.geometry('1280x960')

    #######################################Reference#########################################################

    os.makedirs('Data/images', exist_ok=True)
    pw_left = tk.Frame(root, relief='ridge', borderwidth=6)
    pw_left.pack(side='left', anchor='nw')
    pw_right = tk.Frame(root, relief='ridge', borderwidth=6)
    pw_right.pack(side='top', anchor='e')
    frame1 = tk.Frame(pw_left, bd=2, relief="ridge")
    frame1.pack(fill=tk.X)
    frame2 = tk.LabelFrame(pw_left, bd=2, relief="ridge", text='options')
    frame2.pack(fill=tk.X)
    frame3 = tk.LabelFrame(pw_right, bd=2, text='Uploaded images')
    frame3.pack(fill=tk.Y)
    button = Button(root, frame3)
    label = tk.Label(frame1, text='File:')
    label.pack(fill=tk.X)
    file_name_label = tk.Label(frame1, text='-----not selected-----', width=50, bg='white')
    file_name_label.pack(fill=tk.X)
    select_button = tk.Button(frame1, text='select', command=lambda: button.on_click_select_button(file_name_label))
    select_button.pack(side='left', padx=5, pady=5)
    uploadButton = tk.Button(frame1, text='Upload',
                             command=lambda: button.on_click_upload_button())
    uploadButton.pack(side='left', padx=5, pady=5)

    # gray button
    grayscale_label = tk.Label(frame2, text='gray scale')
    grayscale_label.grid(row=0, column=0)
    gray_show = tk.Button(frame2, text='show',
                          command=lambda: button.on_click_show_button('gray'))
    gray_show.grid(row=0, column=1)

    # binary
    binary_label = tk.Label(frame2, text='binary')
    binary_label.grid(row=1, column=0)
    binary_show = tk.Button(frame2, text='show',
                            command=lambda: button.on_click_show_button('binary'))
    binary_show.grid(row=1, column=1)

    # gaussian blur
    gblur_label = tk.Label(frame2, text='Gaussian blur')
    gblur_label.grid(row=2, column=0)
    gblur_show = tk.Button(frame2, text='show',
                           command=lambda: button.on_click_show_button('gblur'))
    gblur_show.grid(row=2, column=1)

    # canny edge
    canny_label = tk.Label(frame2, text='canny edge')
    canny_label.grid(row=3, column=0)
    canny_show = tk.Button(frame2, text='show',
                           command=lambda: button.on_click_show_button('canny'))
    canny_show.grid(row=3, column=1)

    ######################################################Sample####################################################3333333#
    os.makedirs('Data/Sample_images', exist_ok=True)

    pw_Sample_right = tk.Frame(root, relief='ridge', borderwidth=6)
    pw_Sample_right.pack(side='top', anchor='e')
    frame4 = tk.Frame(pw_left, bd=2, relief="ridge")
    frame4.pack(fill=tk.X)
    frame5 = tk.LabelFrame(pw_left, bd=2, relief="ridge", text='options')
    frame5.pack(fill=tk.X)
    frame6 = tk.LabelFrame(pw_Sample_right, bd=2, text='Uploaded Sample images')
    frame6.pack(fill=tk.Y)

    Sample_button = Sample_Button(root, frame6)
    Sample_label = tk.Label(frame4, text='Sample File:')
    Sample_label.pack(fill=tk.X)
    Sample_file_name_label = tk.Label(frame4, text='-----not selected-----', width=50, bg='white')
    Sample_file_name_label.pack(fill=tk.X)
    Sample_select_button = tk.Button(frame4, text='select',
                                     command=lambda: Sample_button.on_click_select_button_Sample(
                                         Sample_file_name_label))
    Sample_select_button.pack(side='left', padx=5, pady=5)
    Sample_uploadButton = tk.Button(frame4, text='Upload',
                                    command=lambda: Sample_button.on_click_upload_button_Sample())
    Sample_uploadButton.pack(side='left', padx=5, pady=5)

    Sample_grayscale_label = tk.Label(frame5, text='gray scale')
    Sample_grayscale_label.grid(row=0, column=0)
    Sample_gray_show = tk.Button(frame5, text='show',
                                 command=lambda: Sample_button.on_click_show_button_Sample('Sample_gray'))
    Sample_gray_show.grid(row=0, column=1)

    # binary
    Sample_binary_label = tk.Label(frame5, text='binary')
    Sample_binary_label.grid(row=1, column=0)
    Sample_binary_show = tk.Button(frame5, text='show',
                                   command=lambda: Sample_button.on_click_show_button_Sample('Sample_binary'))
    Sample_binary_show.grid(row=1, column=1)

    # gaussian blur
    Sample_gblur_label = tk.Label(frame5, text='Gaussian blur')
    Sample_gblur_label.grid(row=2, column=0)
    Sample_gblur_show = tk.Button(frame5, text='show',
                                  command=lambda: Sample_button.on_click_show_button_Sample('Sample_gblur'))
    Sample_gblur_show.grid(row=2, column=1)

    # canny edge
    Sample_canny_label = tk.Label(frame5, text='canny edge')
    Sample_canny_label.grid(row=3, column=0)
    Sample_canny_show = tk.Button(frame5, text='show',
                                  command=lambda: Sample_button.on_click_show_button_Sample('Sample_canny'))
    Sample_canny_show.grid(row=3, column=1)

    #############################################merged########################################################
    os.makedirs('Data/Differece_images', exist_ok=True)
    frame7 = tk.Frame(pw_left, bd=2, relief="ridge")
    frame7.pack()
    difference_button = Difference_Button(root, frame7)
    Difference_per_label = tk.Label(frame7, text='-----not selected-----', width=50, bg='white', height='12')
    Difference_per_label.pack(fill=tk.X)
    # Diff_label = tk.Label(frame7, textvariable= 'diffvalue', width=40, bg='white', height = '5')
    # Diff_label.pack(fill=tk.X)
    Difference_button = tk.Button(frame7, text='Difference',
                                  command=lambda: difference_button.on_click_diff_per_button(Difference_per_label))
    Difference_button.pack(side='bottom', padx=5, pady=5)

    Reset_button = tk.Button(frame7, text='Reset',
                             command=lambda: difference_button.Reset())
    Reset_button.pack(side='bottom', padx=5, pady=5)
    root.mainloop()