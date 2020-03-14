import setuptools

with open("READ.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name = "MVVM_C_Creator",
  version = "0.0.1",
  author = "Erkan CAN",
  author_email = "erkancan@me.com",
  description = "A small MVVM_C_Creator template",
  long_description = "A small MVVM_C_Creator template for scene",
  url = "https://github.com/erkancan/mvvm_c_creator",
  packages = setuptools.find_packages(),
  classifier = [
      "Programming Language :: Phyton :: 3",
      "Licence :: OSI Approved :: MIT Licence",
      "Operating System :: OS Independent",
      ],
  python_requries = '>=3.0',
  )