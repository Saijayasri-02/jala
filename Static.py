{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ba97f6bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define a static variable and access that through a class.\n",
    "\n",
    "class Python:\n",
    "# Access through class    \n",
    " staticVariable = 9 \n",
    "print(Python.staticVariable)\n",
    "\n",
    "#Change within an class\n",
    "Python.staticVariable = 12\n",
    "print(Python.staticVariable) # Gives 12\n",
    "\n",
    "#Access through an instance\n",
    "instance = Python()\n",
    "print(instance.staticVariable) # Gives 12\n",
    "\n",
    "#Change within an instance\n",
    "instance.staticVariable = 15\n",
    "print(instance.staticVariable) # Gives 15\n",
    "print(Python.staticVariable) #Gives 12"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
