from django.shortcuts import render,HttpResponse ,redirect
from .models import FeedBack 
from .models import Firsts
from datetime import datetime
from django.contrib import messages
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import FileResponse
import os
from PIL import Image
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta



# Create your views here.
def index(request):
    current_datetime = datetime.now()
    return render(request, 'index.html', {'current_datetime': current_datetime})


def feedback(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        feedback = request.POST.get("feedback")
        obj = FeedBack(name=name, phone=phone, email=email, feedback=feedback)
        obj.save()
        print(f"the name is {name}, phone is {phone}, email is {email}, feedback is {feedback}")
        return redirect('success')  # Redirect to the success page upon successful submission

    return render(request, 'feedback.html')


def first(request):
    if request.method == "POST":
        namee = request.POST.get("namee")
        emaill = request.POST.get("emaill")
        phonee = request.POST.get("phonee")
        visit_datee = request.POST.get("visit_datee")
        how_heardd = request.POST.get("how_heardd")
        commentss = request.POST.get("commentss")

        print(f"Debugging: Namee - {namee}")
        print(f"Debugging: Emaill - {emaill}")
        print(f"Debugging: Phonee - {phonee}")
        print(f"Debugging: Visit_datee - {visit_datee}")
        print(f"Debugging: How_heardd - {how_heardd}")
        print(f"Debugging: Commentss - {commentss}")

        # Create and save the object
        obj = Firsts(namee=namee, emaill=emaill, phonee=phonee, visit_datee=visit_datee, how_heardd=how_heardd, commentss=commentss)
        obj.save()

        return redirect('success')  # Redirect to the success page upon successful submission

    return render(request, 'first.html')


    

def bulletins(request):
    return render(request, 'bulletins.html')

def ourministries(request):
    return render(request, 'ourministries.html')

def about(request):
    return render(request, 'about.html')

def preacher(request):
    return render(request, 'preacher.html')

def teaching(request):
    return render(request, 'teaching.html')

def success(request):
    return render(request, 'success.html')
def livestream(request):
    return render(request,'livestream.html')
'''
@login_required(login_url='user_login')
def bulletin(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Redirect authenticated users to another view or home page
        return redirect('bulletin')  # Change 'some_other_view' to the desired URL or view name

    # Redirect non-authenticated users to the login page
    return redirect('user_login')

    # Your other conditions or logic for the bulletin view
    # This code will not be reached if redirections are triggered

  

    return render(request, 'bulletin.html')
'''
def bulletin(request):

    if request.user.is_authenticated:
        return redirect('user_login')
    return redirect ('bulletins.html')


def donate(request):
    return render(request, 'donate.html')

def teaching_sermon(request):
    return render(request, 'teaching_sermon.html')


def teaching2(request):
    return render(request, 'teaching2.html')

def teaching3(request):
    return render(request, 'teaching3.html')

def teaching4(request):
    return render(request, 'teaching4.html')

def teaching5(request):
    return render(request, 'teaching5.html')

def heaven_and_hell(request):
    return render(request, 'heaven_and_hell.html')

def social_vices(request):
    return render(request, 'social_vices.html')

def joy_of_the_lord(request):
    return render(request, 'joy_of_the_lord.html')

def couples_cooperation(request):
    return render(request, 'couples_cooperation.html')

def first_timer(request):
    return render(request, 'first_timer.html')

'''
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                # Redirect to a success page or wherever you want
                return redirect('bulletin')
            
            # Increase the login attempt count
            attempts = request.session.get('login_attempts', 0) + 1
            request.session['login_attempts'] = attempts

            if attempts >= 4:
                # Lock the account for 3 minutes after 4 failed attempts
                request.session['login_locked'] = datetime.now() + timedelta(minutes=3)
                del request.session['login_attempts']
                
                locked_until = request.session.get('login_locked')
                if locked_until and datetime.now() < locked_until:
                    return render(request, 'login_locked.html', {'locked_until': locked_until})
            
            else:
                # Handle invalid login credentials
                error_message = "Invalid login credentials. Please try again."
                return render(request, 'login.html', {'form': form, 'error_message': error_message})

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
'''

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or wherever you want
                return redirect('bulletins')
            
            else:
                # Handle invalid login credentials
                error_message = "Invalid login credentials. Please try again."
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def generate_pdf(request):
    # Specify the directory where you want to save the PDF
    save_directory = "C:/Users/HP/Pictures/Saved Pictures"  # Replace with your desired save directory

    # Ensure the save directory exists, or create it if it doesn't
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # List of image file paths to use for the PDF
    image_filenames = ["C:/Users/HP/Desktop/contactform/form/flask_app/octbulletin.png", "C:/Users/HP/Desktop/contactform/form/flask_app/octbulletin2.png"]  # Replace with your image file names

    # Create a PDF document
    pdf_filename = "january_bulletin.pdf"
    pdf_path = os.path.join(save_directory, pdf_filename)
    c = canvas.Canvas(pdf_path, pagesize=letter)

    # Add each local image to the PDF
    for i, image_filename in enumerate(image_filenames, start=1):
        try:
            image_path = os.path.join(save_directory, image_filename)
            if os.path.exists(image_path):
                # Adjust the position and size as needed for each image
                c.drawImage(image_path, 100, 800 - (i * 350), width=400, height=300)
            else:
                print(f"Image file not found: {image_filename}")
        except Exception as e:
            print(f"Error adding image {i}: {str(e)}")

    # Save the PDF document with all the images
    c.save()

    print(f"PDF with {len(image_filenames)} images saved to {pdf_path}")

    # Serve the generated PDF as a response
    pdf_file = open(pdf_path, "rb")
    response = FileResponse(pdf_file)
    response["Content-Type"] = "application/pdf"
    response["Content-Disposition"] = f'attachment; filename="{pdf_filename}"'
    
    return response 

def february(request):
    # Specify the directory where you want to save the PDF
    save_directory = "C:/Users/HP/Pictures/Saved Pictures"  # Replace with your desired save directory

    # Ensure the save directory exists, or create it if it doesn't
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # List of image file paths to use for the PDF
    image_filenames = ["C:/Users/HP/Desktop/contactform/form/flask_app/octbulletin.png", "C:/Users/HP/Desktop/contactform/form/flask_app/octbulletin2.png"]  # Replace with your image file names

    # Create a PDF document
    pdf_filename = "february_bulletin.pdf"
    pdf_path = os.path.join(save_directory, pdf_filename)
    c = canvas.Canvas(pdf_path, pagesize=letter)

    # Add each local image to the PDF
    for i, image_filename in enumerate(image_filenames, start=1):
        try:
            image_path = os.path.join(save_directory, image_filename)
            if os.path.exists(image_path):
                # Adjust the position and size as needed for each image
                c.drawImage(image_path, 100, 800 - (i * 350), width=400, height=300)
            else:
                print(f"Image file not found: {image_filename}")
        except Exception as e:
            print(f"Error adding image {i}: {str(e)}")

    # Save the PDF document with all the images
    c.save()

    print(f"PDF with {len(image_filenames)} images saved to {pdf_path}")

    # Serve the generated PDF as a response
    pdf_file = open(pdf_path, "rb")
    response = FileResponse(pdf_file)
    response["Content-Type"] = "application/pdf"
    response["Content-Disposition"] = f'attachment; filename="{pdf_filename}"'
    
    return response 


def march(request):
    # Specify the directory where you want to save the PDF
    save_directory = "C:/Users/HP/Pictures/Saved Pictures"  # Replace with your desired save directory

    # Ensure the save directory exists, or create it if it doesn't
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # List of image file paths to use for the PDF
    image_filenames = ["C:/Users/HP/Desktop/contactform/form/flask_app/octbulletin.png", "C:/Users/HP/Desktop/contactform/form/flask_app/octbulletin2.png"]  # Replace with your image file names

    # Create a PDF document
    pdf_filename = "march_bulletin.pdf"
    pdf_path = os.path.join(save_directory, pdf_filename)
    c = canvas.Canvas(pdf_path, pagesize=letter)

    # Add each local image to the PDF
    for i, image_filename in enumerate(image_filenames, start=1):
        try:
            image_path = os.path.join(save_directory, image_filename)
            if os.path.exists(image_path):
                # Adjust the position and size as needed for each image
                c.drawImage(image_path, 100, 800 - (i * 350), width=400, height=300)
            else:
                print(f"Image file not found: {image_filename}")
        except Exception as e:
            print(f"Error adding image {i}: {str(e)}")

    # Save the PDF document with all the images
    c.save()

    print(f"PDF with {len(image_filenames)} images saved to {pdf_path}")

    # Serve the generated PDF as a response
    pdf_file = open(pdf_path, "rb")
    response = FileResponse(pdf_file)
    response["Content-Type"] = "application/pdf"
    response["Content-Disposition"] = f'attachment; filename="{pdf_filename}"'
    
    return response 


def april(request):
    # Specify the directory where you want to save the PDF
    save_directory = "C:/Users/HP/Pictures/Saved Pictures"  # Replace with your desired save directory

    # Ensure the save directory exists, or create it if it doesn't
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # List of image file paths to use for the PDF
    image_filenames = ["C:/Users/HP/Desktop/contactform/form/flask_app/octbulletin.png", "C:/Users/HP/Desktop/contactform/form/flask_app/octbulletin2.png"]  # Replace with your image file names

    # Create a PDF document
    pdf_filename = "april_bulletin.pdf"
    pdf_path = os.path.join(save_directory, pdf_filename)
    c = canvas.Canvas(pdf_path, pagesize=letter)

    # Add each local image to the PDF
    for i, image_filename in enumerate(image_filenames, start=1):
        try:
            image_path = os.path.join(save_directory, image_filename)
            if os.path.exists(image_path):
                # Adjust the position and size as needed for each image
                c.drawImage(image_path, 100, 800 - (i * 350), width=400, height=300)
            else:
                print(f"Image file not found: {image_filename}")
        except Exception as e:
            print(f"Error adding image {i}: {str(e)}")

    # Save the PDF document with all the images
    c.save()

    print(f"PDF with {len(image_filenames)} images saved to {pdf_path}")

    # Serve the generated PDF as a response
    pdf_file = open(pdf_path, "rb")
    response = FileResponse(pdf_file)
    response["Content-Type"] = "application/pdf"
    response["Content-Disposition"] = f'attachment; filename="{pdf_filename}"'
    
    return response 


def may(request):
    # Specify the directory where you want to save the PDF
    save_directory = "C:/Users/HP/Pictures/Saved Pictures"  # Replace with your desired save directory

    # Ensure the save directory exists, or create it if it doesn't
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # List of image file paths to use for the PDF
    image_filenames = ["C:/Users/HP/Desktop/contactform/form/flask_app/octbulletin.png", "C:/Users/HP/Desktop/contactform/form/flask_app/octbulletin2.png"]  # Replace with your image file names

    # Create a PDF document
    pdf_filename = "may_bulletin.pdf"
    pdf_path = os.path.join(save_directory, pdf_filename)
    c = canvas.Canvas(pdf_path, pagesize=letter)

    # Add each local image to the PDF
    for i, image_filename in enumerate(image_filenames, start=1):
        try:
            image_path = os.path.join(save_directory, image_filename)
            if os.path.exists(image_path):
                # Adjust the position and size as needed for each image
                c.drawImage(image_path, 100, 800 - (i * 350), width=400, height=300)
            else:
                print(f"Image file not found: {image_filename}")
        except Exception as e:
            print(f"Error adding image {i}: {str(e)}")

    # Save the PDF document with all the images
    c.save()

    print(f"PDF with {len(image_filenames)} images saved to {pdf_path}")

    # Serve the generated PDF as a response
    pdf_file = open(pdf_path, "rb")
    response = FileResponse(pdf_file)
    response["Content-Type"] = "application/pdf"
    response["Content-Disposition"] = f'attachment; filename="{pdf_filename}"'
    
    return response 


def june(request):
    # Specify the directory where you want to save the PDF
    save_directory = "C:/Users/HP/Pictures/Saved Pictures"  # Replace with your desired save directory

    # Ensure the save directory exists, or create it if it doesn't
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # List of image file paths to use for the PDF
    image_filenames = ["C:/Users/HP/Desktop/contactform/form/flask_app/octbulletin.png", "C:/Users/HP/Desktop/contactform/form/flask_app/octbulletin2.png"]  # Replace with your image file names

    # Create a PDF document
    pdf_filename = "june_bulletin.pdf"
    pdf_path = os.path.join(save_directory, pdf_filename)
    c = canvas.Canvas(pdf_path, pagesize=letter)

    # Add each local image to the PDF
    for i, image_filename in enumerate(image_filenames, start=1):
        try:
            image_path = os.path.join(save_directory, image_filename)
            if os.path.exists(image_path):
                # Adjust the position and size as needed for each image
                c.drawImage(image_path, 100, 800 - (i * 350), width=400, height=300)
            else:
                print(f"Image file not found: {image_filename}")
        except Exception as e:
            print(f"Error adding image {i}: {str(e)}")

    # Save the PDF document with all the images
    c.save()

    print(f"PDF with {len(image_filenames)} images saved to {pdf_path}")

    # Serve the generated PDF as a response
    pdf_file = open(pdf_path, "rb")
    response = FileResponse(pdf_file)
    response["Content-Type"] = "application/pdf"
    response["Content-Disposition"] = f'attachment; filename="{pdf_filename}"'
    
    return response 


def july(request):
    # Specify the directory where you want to save the PDF
    save_directory = "C:/Users/HP/Pictures/Saved Pictures"  # Replace with your desired save directory

    # Ensure the save directory exists, or create it if it doesn't
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # List of image file paths to use for the PDF
    image_filenames = ["C:/Users/HP/Desktop/contactform/form/flask_app/octbulletin.png", "C:/Users/HP/Desktop/contactform/form/flask_app/octbulletin2.png"]  # Replace with your image file names

    # Create a PDF document
    pdf_filename = "july_bulletin.pdf"
    pdf_path = os.path.join(save_directory, pdf_filename)
    c = canvas.Canvas(pdf_path, pagesize=letter)

    # Add each local image to the PDF
    for i, image_filename in enumerate(image_filenames, start=1):
        try:
            image_path = os.path.join(save_directory, image_filename)
            if os.path.exists(image_path):
                # Adjust the position and size as needed for each image
                c.drawImage(image_path, 100, 800 - (i * 350), width=400, height=300)
            else:
                print(f"Image file not found: {image_filename}")
        except Exception as e:
            print(f"Error adding image {i}: {str(e)}")

    # Save the PDF document with all the images
    c.save()

    print(f"PDF with {len(image_filenames)} images saved to {pdf_path}")

    # Serve the generated PDF as a response
    pdf_file = open(pdf_path, "rb")
    response = FileResponse(pdf_file)
    response["Content-Type"] = "application/pdf"
    response["Content-Disposition"] = f'attachment; filename="{pdf_filename}"'
    
    return response 

def august(request):
    # Specify the directory where you want to save the PDF
    save_directory = "C:/Users/HP/Pictures/Saved Pictures"  # Replace with your desired save directory

    # Ensure the save directory exists, or create it if it doesn't
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # List of image file paths to use for the PDF
    image_filenames = ["C:/Users/HP/Desktop/contactform/form/flask_app/octbulletin.png", "C:/Users/HP/Desktop/contactform/form/flask_app/octbulletin2.png"]  # Replace with your image file names

    # Create a PDF document
    pdf_filename = "august_bulletin.pdf"
    pdf_path = os.path.join(save_directory, pdf_filename)
    c = canvas.Canvas(pdf_path, pagesize=letter)

    # Add each local image to the PDF
    for i, image_filename in enumerate(image_filenames, start=1):
        try:
            image_path = os.path.join(save_directory, image_filename)
            if os.path.exists(image_path):
                # Adjust the position and size as needed for each image
                c.drawImage(image_path, 100, 800 - (i * 350), width=400, height=300)
            else:
                print(f"Image file not found: {image_filename}")
        except Exception as e:
            print(f"Error adding image {i}: {str(e)}")

    # Save the PDF document with all the images
    c.save()

    print(f"PDF with {len(image_filenames)} images saved to {pdf_path}")

    # Serve the generated PDF as a response
    pdf_file = open(pdf_path, "rb")
    response = FileResponse(pdf_file)
    response["Content-Type"] = "application/pdf"
    response["Content-Disposition"] = f'attachment; filename="{pdf_filename}"'
    
    return response 

def september(request):
    # Specify the directory where you want to save the PDF
    save_directory = "C:/Users/HP/Pictures/Saved Pictures"  # Replace with your desired save directory

    # Ensure the save directory exists, or create it if it doesn't
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # List of image file paths to use for the PDF
    image_filenames = ["C:/Users/HP/Desktop/contactform/form/flask_app/octbulletin.png", "C:/Users/HP/Desktop/contactform/form/flask_app/octbulletin2.png"]  # Replace with your image file names

    # Create a PDF document
    pdf_filename = "september_bulletin.pdf"
    pdf_path = os.path.join(save_directory, pdf_filename)
    c = canvas.Canvas(pdf_path, pagesize=letter)

    # Add each local image to the PDF
    for i, image_filename in enumerate(image_filenames, start=1):
        try:
            image_path = os.path.join(save_directory, image_filename)
            if os.path.exists(image_path):
                # Adjust the position and size as needed for each image
                c.drawImage(image_path, 100, 800 - (i * 350), width=400, height=300)
            else:
                print(f"Image file not found: {image_filename}")
        except Exception as e:
            print(f"Error adding image {i}: {str(e)}")

    # Save the PDF document with all the images
    c.save()

    print(f"PDF with {len(image_filenames)} images saved to {pdf_path}")

    # Serve the generated PDF as a response
    pdf_file = open(pdf_path, "rb")
    response = FileResponse(pdf_file)
    response["Content-Type"] = "application/pdf"
    response["Content-Disposition"] = f'attachment; filename="{pdf_filename}"'
    
    return response 

def october(request):
    # Specify the directory where you want to save the PDF
    save_directory = "C:/Users/HP/Pictures/Saved Pictures"  # Replace with your desired save directory

    # Ensure the save directory exists, or create it if it doesn't
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # List of image file paths to use for the PDF
    image_filenames = ["C:/Users/HP/Desktop/contactform/form/flask_app/octbulletin.png", "C:/Users/HP/Desktop/contactform/form/flask_app/octbulletin2.png"]  # Replace with your image file names

    # Create a PDF document
    pdf_filename = "october_bulletin.pdf"
    pdf_path = os.path.join(save_directory, pdf_filename)
    c = canvas.Canvas(pdf_path, pagesize=letter)

    # Add each local image to the PDF
    for i, image_filename in enumerate(image_filenames, start=1):
        try:
            image_path = os.path.join(save_directory, image_filename)
            if os.path.exists(image_path):
                # Adjust the position and size as needed for each image
                c.drawImage(image_path, 100, 800 - (i * 350), width=400, height=300)
            else:
                print(f"Image file not found: {image_filename}")
        except Exception as e:
            print(f"Error adding image {i}: {str(e)}")

    # Save the PDF document with all the images
    c.save()

    print(f"PDF with {len(image_filenames)} images saved to {pdf_path}")

    # Serve the generated PDF as a response
    pdf_file = open(pdf_path, "rb")
    response = FileResponse(pdf_file)
    response["Content-Type"] = "application/pdf"
    response["Content-Disposition"] = f'attachment; filename="{pdf_filename}"'
    
    return response 

def november(request):
    # Specify the directory where you want to save the PDF
    save_directory = "C:/Users/HP/Pictures/Saved Pictures"  # Replace with your desired save directory

    # Ensure the save directory exists, or create it if it doesn't
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # List of image file paths to use for the PDF
    image_filenames = ["C:/Users/HP/Desktop/contactform/form/flask_app/nov.png", "C:/Users/HP/Desktop/contactform/form/flask_app/nov2.png"]  # Replace with your image file names

    # Create a PDF document
    pdf_filename = "november_bulletin.pdf"
    pdf_path = os.path.join(save_directory, pdf_filename)
    c = canvas.Canvas(pdf_path, pagesize=letter)

    # Add each local image to the PDF
    for i, image_filename in enumerate(image_filenames, start=1):
        try:
            image_path = os.path.join(save_directory, image_filename)
            if os.path.exists(image_path):
                # Adjust the position and size as needed for each image
                c.drawImage(image_path, 100, 800 - (i * 350), width=400, height=300)
            else:
                print(f"Image file not found: {image_filename}")
        except Exception as e:
            print(f"Error adding image {i}: {str(e)}")

    # Save the PDF document with all the images
    c.save()

    print(f"PDF with {len(image_filenames)} images saved to {pdf_path}")

    # Serve the generated PDF as a response
    pdf_file = open(pdf_path, "rb")
    response = FileResponse(pdf_file)
    response["Content-Type"] = "application/pdf"
    response["Content-Disposition"] = f'attachment; filename="{pdf_filename}"'
    
    return response 

def december(request):
    # Specify the directory where you want to save the PDF
    save_directory = "C:/Users/HP/Pictures/Saved Pictures"  # Replace with your desired save directory

    # Ensure the save directory exists, or create it if it doesn't
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # List of image file paths to use for the PDF
    image_filenames = ["C:/Users/HP/Desktop/contactform/form/flask_app/octbulletin.png", "C:/Users/HP/Desktop/contactform/form/flask_app/octbulletin2.png"]  # Replace with your image file names

    # Create a PDF document
    pdf_filename = "december_bulletin.pdf"
    pdf_path = os.path.join(save_directory, pdf_filename)
    c = canvas.Canvas(pdf_path, pagesize=letter)

    # Add each local image to the PDF
    for i, image_filename in enumerate(image_filenames, start=1):
        try:
            image_path = os.path.join(save_directory, image_filename)
            if os.path.exists(image_path):
                # Adjust the position and size as needed for each image
                c.drawImage(image_path, 100, 800 - (i * 350), width=400, height=300)
            else:
                print(f"Image file not found: {image_filename}")
        except Exception as e:
            print(f"Error adding image {i}: {str(e)}")

    # Save the PDF document with all the images
    c.save()

    print(f"PDF with {len(image_filenames)} images saved to {pdf_path}")

    # Serve the generated PDF as a response
    pdf_file = open(pdf_path, "rb")
    response = FileResponse(pdf_file)
    response["Content-Type"] = "application/pdf"
    response["Content-Disposition"] = f'attachment; filename="{pdf_filename}"'
    
    return response 



def jan(request):
    return render(request, 'generate_pdf.html')

def feb(request):
    return render(request, 'february.html')

def mar(request):
    return render(request, 'march.html')
    
def apr(request):
    return render(request, 'april.html')

def may_b(request):
    return render(request, 'may.html')

def jun(request):
    return render(request, 'june.html')

def jul(request):
    return render(request, 'july.html')

def aug(request):
    return render(request, 'august.html')

def sep(request):
    return render(request, 'september.html')

def oct(request):
    return render(request, 'october.html')

def nov(request):
    return render(request, 'november.html')

def dec(request):
    return render(request, 'december.html')