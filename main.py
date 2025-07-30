from customtkinter import *
from PIL import Image , ImageTk  , ImageEnhance , ImageFilter
from tkinter import filedialog 

class App(CTk): 
    picture = Image.open("picture.jpg")
    new_picture = None

    def __init__(self):
        super(App,self).__init__()

        # Variables
        self.var_Brightness = DoubleVar()
        self.var_Color = DoubleVar()
        self.var_Sharpness = DoubleVar()
        self.blur = BooleanVar()
        self.EMBOSS = BooleanVar()
        self.FIND_EDGES = BooleanVar()
        self.SMOOTH = BooleanVar()  
        self.SMOOTH_MORE = BooleanVar() 
        self.EDGE_MORE = BooleanVar()
        self.EDGE = BooleanVar()
        self.DETAIL = BooleanVar()
        self.CONTOUR = BooleanVar()
        self.SHARPEN = BooleanVar()
        self.var_MinFilter = IntVar()
        self.var_MedianFilter = IntVar()
        self.var_MaxFilter = IntVar()
        self.var_ModeFilter = IntVar()
        self.var_BoxBlur = IntVar()
        self.var_GaussianBlur = IntVar()
        self.var_UnsharpMask = IntVar()

        # info
        self.title("Photo Editor")
        self.geometry("900x400")
        self.resizable(0,0)

        # main
        self.run()
        self.mainloop()

    def run(self):

        def open_image():
            self.picture = Image.open(filedialog.askopenfile().name)
            self.var_BoxBlur.set(0)
            self.var_Brightness.set(0)
            self.var_Color.set(0)
            self.var_GaussianBlur.set(0)
            self.var_MaxFilter.set(0)
            self.var_MedianFilter.set(0)
            self.var_MinFilter.set(0)
            self.var_ModeFilter.set(0)
            self.var_Sharpness.set(0)
            self.var_UnsharpMask.set(0)
            self.edit_img()
        
        CTkButton(self,width=333,text="Open Picture",command=open_image).pack(side="top",anchor="e")
        self.frame_photo = CTkFrame(self)
        self.frame_photo.pack(expand= 1,side='left')

        self.label_img = CTkLabel(self.frame_photo,image= ImageTk.PhotoImage(self.picture.resize((self.picture.size[0]*2,self.picture.size[1]*2))),text='')
        self.label_img.pack(expand='y')

        self.enhance()
        
    def show_edit(self,value):
        self.frame_edit = CTkFrame(self)
        self.frame_edit.pack(expand= 1,side='left',fill='both')
        
        edit_mode = ["Enhance","Filter"]
        var = StringVar(value=value)
        edit_combo_box = CTkComboBox(self.frame_edit,width=250,variable= var
            ,values= edit_mode,justify="center",command= self.set_edit)
        
        edit_combo_box.pack(fill="y",pady= 10)
        
    def set_edit(self,value):
        self.frame_edit.destroy()
        match value:
            case "Enhance":
                self.enhance()
            case "Filter":
                self.filter()

    def filter(self):
        self.show_edit("Filter")
        self.frame_scroll = CTkScrollableFrame(self.frame_edit,)
        self.frame_scroll.pack(expand= 1,fill='both',side="bottom")
    
# ---- BLUR -------------------------------------------------------------------------------------------------------------------------
   
        CTkSwitch(master= self.frame_scroll,text='   BLUR',variable=self.blur,font=('arial',20),command=self.edit_img).pack(pady=5 ,expand=1 , fill='both',padx=(50,1))

# ---- SMOOTH -------------------------------------------------------------------------------------------------------------------------
   
        CTkSwitch(master= self.frame_scroll,text='   SMOOTH',variable=self.SMOOTH,font=('arial',20),command=self.edit_img).pack(pady=5 ,expand=1 , fill='both',padx=(50,1))

# ---- SMOOTH MORE -------------------------------------------------------------------------------------------------------------------------
   
        CTkSwitch(master= self.frame_scroll,text='   SMOOTH MORE',variable=self.SMOOTH_MORE,font=('arial',20),command=self.edit_img).pack(pady=5,expand=1 , fill='both',padx=(50,1))

# ---- SHARPEN -------------------------------------------------------------------------------------------------------------------------
   
        CTkSwitch(master= self.frame_scroll,text='   SHARPEN',variable=self.SHARPEN,font=('arial',20),command=self.edit_img).pack(pady=5,expand=1 , fill='both',padx=(50,1))

# ---- CONTOUR -------------------------------------------------------------------------------------------------------------------------
   
        CTkSwitch(master= self.frame_scroll,text='   CONTOUR',variable=self.CONTOUR,font=('arial',20),command=self.edit_img).pack(pady=5,expand=1 , fill='both',padx=(50,1))
 
# ---- DETAIL -------------------------------------------------------------------------------------------------------------------------
          
        CTkSwitch(master= self.frame_scroll,text='   DETAIL',variable=self.DETAIL,font=('arial',20),command=self.edit_img).pack(pady=5,expand=1 , fill='both',padx=(50,1))

# ---- EDGE -------------------------------------------------------------------------------------------------------------------------
   
        CTkSwitch(master= self.frame_scroll,text='   EDGE',variable=self.EDGE,font=('arial',20),command=self.edit_img).pack(pady=5,expand=1 , fill='both',padx=(50,1))

# ---- EDGE MORE -------------------------------------------------------------------------------------------------------------------------
   
        CTkSwitch(master= self.frame_scroll,text='   EDGE MORE',variable=self.EDGE_MORE,font=('arial',20),command=self.edit_img).pack(pady=5,expand=1 , fill='both',padx=(50,1))

# ---- FIND EDGES -------------------------------------------------------------------------------------------------------------------------
      
        CTkSwitch(master= self.frame_scroll,text='   FIND EDGES',variable=self.FIND_EDGES,font=('arial',20),command=self.edit_img).pack(pady=5,expand=1 , fill='both',padx=(50,1))

# ---- EMBOSS -------------------------------------------------------------------------------------------------------------------------
 
        CTkSwitch(master= self.frame_scroll,text='   EMBOSS',variable=self.EMBOSS,font=('arial',20),command=self.edit_img).pack(pady=5,expand=1 , fill='both',padx=(50,1))

# ---- MinFilter -------------------------------------------------------------------------------------------------------------------------

        frameMinFilter = CTkFrame(self.frame_scroll) ; frameMinFilter.pack(pady=5,expand=1 , fill='both',padx=(50,1))
        
        chack_min = BooleanVar()
        def set_MinFilter():
            MinFilterSlider = CTkSlider(variable=self.var_MinFilter,master=frameMinFilter
                                        ,from_=1,to=9,number_of_steps=4,width=250,command=lambda x:self.edit_img())
            if chack_min.get():
                MinFilterSlider.pack(pady=(3,20))
            else:
                self.var_MinFilter.set(0)
                self.edit_img()
                for objact in list(frameMinFilter.children.keys())[2:]:
                    frameMinFilter.children[objact].destroy()

        CTkSwitch(master= frameMinFilter,text='   Min Filter',font=('arial',20)
                  ,command=set_MinFilter,variable=chack_min).pack(pady=5,expand=1 , fill='both')

# ---- MedianFilter -------------------------------------------------------------------------------------------------------------------------

        frameMedianFilter = CTkFrame(self.frame_scroll) ; frameMedianFilter.pack(pady=5,expand=1 , fill='both',padx=(50,1))
        
        chack_median = BooleanVar()
        def set_MedianFilter():
            MedianFilterSlider = CTkSlider(frameMedianFilter,width=250,from_=1,to=9,number_of_steps=4,
                                           variable=self.var_MedianFilter,command=lambda x:self.edit_img())
            if chack_median.get():
                MedianFilterSlider.pack(pady=(3,20))
            else:
                self.var_MedianFilter.set(0)
                self.edit_img()
                for objact in list(frameMedianFilter.children.keys())[2:]:
                    frameMedianFilter.children[objact].destroy()

        CTkSwitch(master= frameMedianFilter,text='   Median Filter',font=('arial',20)
                  ,command=set_MedianFilter,variable=chack_median).pack(pady=5,expand=1 , fill='both')

# ---- MaxFilter -------------------------------------------------------------------------------------------------------------------------

        frameMaxFilter = CTkFrame(self.frame_scroll) ; frameMaxFilter.pack(pady=5,expand=1 , fill='both',padx=(50,1))
        
        chack_max = BooleanVar()
        def set_MaxFilter():
            MaxFilterSlider = CTkSlider(frameMaxFilter,width=250,from_=1,to=9,number_of_steps=4,
                                           variable=self.var_MaxFilter,command=lambda x:self.edit_img())
            if chack_max.get():
                MaxFilterSlider.pack(pady=(3,20))
            else:
                self.var_MaxFilter.set(0)
                self.edit_img()
                for objact in list(frameMaxFilter.children.keys())[2:]:
                    frameMaxFilter.children[objact].destroy()

        CTkSwitch(master= frameMaxFilter,text='   Max Filter',font=('arial',20)
                  ,command=set_MaxFilter,variable=chack_max).pack(pady=5,expand=1 , fill='both')

# ---- ModeFilter -------------------------------------------------------------------------------------------------------------------------

        frameModeFilter = CTkFrame(self.frame_scroll) ; frameModeFilter.pack(pady=5,expand=1 , fill='both',padx=(50,1))
        
        chack_mode = BooleanVar()
        def set_ModeFilter():
            ModeFilterSwitch = CTkSlider(frameModeFilter,width=250,from_=1,to=9,number_of_steps=4,
                                           variable=self.var_ModeFilter,command=lambda x:self.edit_img())
            if chack_mode.get():
                ModeFilterSwitch.pack(pady=(3,20))
            else:
                self.var_ModeFilter.set(0)
                self.edit_img()
                for objact in list(frameModeFilter.children.keys())[2:]:
                    frameModeFilter.children[objact].destroy()

        CTkSwitch(master= frameModeFilter,text='   Mode Filter',font=('arial',20)
                  ,command=set_ModeFilter,variable=chack_mode).pack(pady=5,expand=1 , fill='both')

# ---- BoxBlur -------------------------------------------------------------------------------------------------------------------------

        frameBoxBlur = CTkFrame(self.frame_scroll) ; frameBoxBlur.pack(pady=5,expand=1 , fill='both',padx=(50,1))
        
        chack_boxblur = BooleanVar()
        def set_BoxBlur():
            BoxBlurSwitch = CTkSlider(frameBoxBlur,width=250,from_=1,to=9,number_of_steps=4,
                                           variable=self.var_BoxBlur,command=lambda x:self.edit_img())
            if chack_boxblur.get():
                BoxBlurSwitch.pack(pady=(3,20))
            else:
                self.var_BoxBlur.set(0)
                self.edit_img()
                for objact in list(frameBoxBlur.children.keys())[2:]:
                    frameBoxBlur.children[objact].destroy()

        CTkSwitch(master= frameBoxBlur,text='   Box Blur',font=('arial',20)
                  ,command=set_BoxBlur,variable=chack_boxblur).pack(pady=5,expand=1 , fill='both')

# ---- GaussianBlur -------------------------------------------------------------------------------------------------------------------------

        frameGaussianBlur = CTkFrame(self.frame_scroll) ; frameGaussianBlur.pack(pady=5,expand=1 , fill='both',padx=(50,1))
        
        chack_gaussianblur = BooleanVar()
        def set_GaussianBlur():
            GaussianBlurSwitch = CTkSlider(frameGaussianBlur,width=250,from_=1,to=9,number_of_steps=4,
                                           variable=self.var_GaussianBlur,command=lambda x:self.edit_img())
            if chack_gaussianblur.get():
                GaussianBlurSwitch.pack(pady=(3,20))
            else:
                self.var_GaussianBlur.set(0)
                self.edit_img()
                for objact in list(frameGaussianBlur.children.keys())[2:]:
                    frameGaussianBlur.children[objact].destroy()

        CTkSwitch(master= frameGaussianBlur,text='   Gaussian Blur',font=('arial',20)
                  ,command=set_GaussianBlur,variable=chack_gaussianblur).pack(pady=5,expand=1 , fill='both')

# ---- UnsharpMask -------------------------------------------------------------------------------------------------------------------------
        
        frameUnsharpMask = CTkFrame(self.frame_scroll) ; frameUnsharpMask.pack(pady=5,expand=1 , fill='both',padx=(50,1))
        
        chack_unsharpmask = BooleanVar()
        def set_UnsharpMask():
            UnsharpMaskSwitch = CTkSlider(frameUnsharpMask,width=250,from_=1,to=9,number_of_steps=4,
                                           variable=self.var_UnsharpMask,command=lambda x:self.edit_img())
            if chack_unsharpmask.get():
                UnsharpMaskSwitch.pack(pady=(3,20))
            else:
                self.var_UnsharpMask.set(0)
                self.edit_img()
                for objact in list(frameUnsharpMask.children.keys())[2:]:
                    frameUnsharpMask.children[objact].destroy()

        CTkSwitch(master= frameUnsharpMask,text='   Unsharp Mask',font=('arial',20)
                  ,command=set_UnsharpMask,variable=chack_unsharpmask).pack(pady=5,expand=1 , fill='both')

        CTkFrame(self.frame_scroll,fg_color='gray20').pack(pady=5,expand=1 , fill='both',padx=(50,1))
        
    def enhance(self):
        self.show_edit("Enhance")
        self.frame_scroll = CTkFrame(self.frame_edit,)
        self.frame_scroll.pack(expand= 1,fill='both',side="bottom")

# ---- Brightness -------------------------------------------------------------------------------------------------------------------------
   
        CTkLabel(master= self.frame_scroll,text="Brightness :",font=("arial",20)).pack()
        CTkSlider(self.frame_scroll
                  ,width=250,variable=self.var_Brightness
                  ,command= lambda x : self.edit_img()
                  ,from_= -10
                  ,to= 10,).pack(pady=(3,20))

# ---- Color -------------------------------------------------------------------------------------------------------------------------
   
        CTkLabel(master= self.frame_scroll,text="Color :",font=("arial",20)).pack()
        CTkSlider(self.frame_scroll,width=250,variable=self.var_Color
                  ,command= lambda x : self.edit_img()
                  ,from_= -10
                  ,to= 10,).pack(pady=(3,20))

# ---- Sharpness -------------------------------------------------------------------------------------------------------------------------
   
        CTkLabel(master= self.frame_scroll,text="Sharpness :",font=("arial",20)).pack()
        CTkSlider(self.frame_scroll,width=250,variable=self.var_Sharpness
                  ,command= lambda x : self.edit_img()
                  ,from_= -10
                  ,to= 10).pack(pady=(3,20))
    
    def edit_img(self):
        self.new_picture = self.picture.copy().resize((self.picture.size[0]*2,self.picture.size[1]*2))
        if self.var_Brightness.get():
            self.new_picture = ImageEnhance.Brightness(self.new_picture)
            self.new_picture.enhance(self.var_Brightness.get())\
            .save("new_picture.png")
        else:
            self.new_picture.save("new_picture.png")

        if self.var_Color.get():
            self.new_picture = Image.open("new_picture.png").resize((self.picture.size[0]*2,self.picture.size[1]*2))
            self.new_picture = ImageEnhance.Color(self.new_picture)
            self.new_picture.enhance(self.var_Color.get()).save("new_picture.png")
        
        if self.var_Sharpness.get():
            self.new_picture = Image.open("new_picture.png").resize((self.picture.size[0]*2,self.picture.size[1]*2))
            self.new_picture = ImageEnhance.Sharpness(self.new_picture)
            self.new_picture.enhance(self.var_Sharpness.get()).save("new_picture.png")
        
        if self.blur.get():
            self.new_picture = Image.open("new_picture.png").resize((self.picture.size[0]*2,self.picture.size[1]*2))
            self.new_picture = self.new_picture.filter(ImageFilter.BLUR)
            self.new_picture.save("new_picture.png")
        
        if self.SMOOTH.get():
            self.new_picture = Image.open("new_picture.png").resize((self.picture.size[0]*2,self.picture.size[1]*2))
            self.new_picture = self.new_picture.filter(ImageFilter.SMOOTH)
            self.new_picture.save("new_picture.png")
        
        if self.SMOOTH_MORE.get():
            self.new_picture = Image.open("new_picture.png").resize((self.picture.size[0]*2,self.picture.size[1]*2))
            self.new_picture = self.new_picture.filter(ImageFilter.SMOOTH_MORE)
            self.new_picture.save("new_picture.png")
        
        if self.SHARPEN.get():
            self.new_picture = Image.open("new_picture.png").resize((self.picture.size[0]*2,self.picture.size[1]*2))
            self.new_picture = self.new_picture.filter(ImageFilter.SHARPEN)
            self.new_picture.save("new_picture.png")
        
        if self.CONTOUR.get():
            self.new_picture = Image.open("new_picture.png").resize((self.picture.size[0]*2,self.picture.size[1]*2))
            self.new_picture = self.new_picture.filter(ImageFilter.CONTOUR)
            self.new_picture.save("new_picture.png")

        if self.DETAIL.get():
            self.new_picture = Image.open("new_picture.png").resize((self.picture.size[0]*2,self.picture.size[1]*2))
            self.new_picture = self.new_picture.filter(ImageFilter.DETAIL)
            self.new_picture.save("new_picture.png")
        
        if self.EDGE.get():
            self.new_picture = Image.open("new_picture.png").resize((self.picture.size[0]*2,self.picture.size[1]*2))
            self.new_picture = self.new_picture.filter(ImageFilter.EDGE_ENHANCE)
            self.new_picture.save("new_picture.png")
        
        if self.EDGE_MORE.get():
            self.new_picture = Image.open("new_picture.png").resize((self.picture.size[0]*2,self.picture.size[1]*2))
            self.new_picture = self.new_picture.filter(ImageFilter.EDGE_ENHANCE_MORE)
            self.new_picture.save("new_picture.png")
        
        if self.FIND_EDGES.get():
            self.new_picture = Image.open("new_picture.png").resize((self.picture.size[0]*2,self.picture.size[1]*2))
            self.new_picture = self.new_picture.filter(ImageFilter.FIND_EDGES)
            self.new_picture.save("new_picture.png")
        
        if self.EMBOSS.get():
            self.new_picture = Image.open("new_picture.png").resize((self.picture.size[0]*2,self.picture.size[1]*2))
            self.new_picture = self.new_picture.filter(ImageFilter.EMBOSS)
            self.new_picture.save("new_picture.png")
        
        if self.var_MinFilter.get():
            self.new_picture = Image.open("new_picture.png").resize((self.picture.size[0]*2,self.picture.size[1]*2))
            self.new_picture = self.new_picture.filter(ImageFilter.MinFilter(self.var_MinFilter.get()))
            self.new_picture.save("new_picture.png")
        
        if self.var_MedianFilter.get():
            self.new_picture = Image.open("new_picture.png").resize((self.picture.size[0]*2,self.picture.size[1]*2))
            self.new_picture = self.new_picture.filter(ImageFilter.MedianFilter(self.var_MedianFilter.get()))
            self.new_picture.save("new_picture.png")
        
        if self.var_MaxFilter.get():
            self.new_picture = Image.open("new_picture.png").resize((self.picture.size[0]*2,self.picture.size[1]*2))
            self.new_picture = self.new_picture.filter(ImageFilter.MaxFilter(self.var_MaxFilter.get()))
            self.new_picture.save("new_picture.png")
        
        if self.var_ModeFilter.get():
            self.new_picture = Image.open("new_picture.png").resize((self.picture.size[0]*2,self.picture.size[1]*2))
            self.new_picture = self.new_picture.filter(ImageFilter.ModeFilter(self.var_ModeFilter.get()))
            self.new_picture.save("new_picture.png")
        
        if self.var_BoxBlur.get():
            self.new_picture = Image.open("new_picture.png").resize((self.picture.size[0]*2,self.picture.size[1]*2))
            self.new_picture = self.new_picture.filter(ImageFilter.BoxBlur(self.var_BoxBlur.get()))
            self.new_picture.save("new_picture.png")
        
        if self.var_MaxFilter.get():
            self.new_picture = Image.open("new_picture.png").resize((self.picture.size[0]*2,self.picture.size[1]*2))
            self.new_picture = self.new_picture.filter(ImageFilter.MaxFilter(self.var_MaxFilter.get()))
            self.new_picture.save("new_picture.png")
        
        if self.var_GaussianBlur.get():
            self.new_picture = Image.open("new_picture.png").resize((self.picture.size[0]*2,self.picture.size[1]*2))
            self.new_picture = self.new_picture.filter(ImageFilter.GaussianBlur(self.var_GaussianBlur.get()))
            self.new_picture.save("new_picture.png")
        
        if self.var_UnsharpMask.get():
            self.new_picture = Image.open("new_picture.png").resize((self.picture.size[0]*2,self.picture.size[1]*2))
            self.new_picture = self.new_picture.filter(ImageFilter.GaussianBlur(self.var_GaussianBlur.get()))
            self.new_picture.save("new_picture.png")

        self.label_img.configure(image=ImageTk.PhotoImage(Image.open("new_picture.png")))

if __name__ == "__main__":
    App()