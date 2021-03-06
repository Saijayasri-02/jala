{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8f89c7bf",
   "metadata": {},
   "outputs": [],
   "source": [
    "from abc import ABC, abstractmethod\n",
    " \n",
    "class Polygon(ABC): #base class / super class\n",
    " \n",
    "    @abstractmethod\n",
    "    def noofsides(self):\n",
    "        pass\n",
    " \n",
    "class Triangle(Polygon): #subclass\n",
    " \n",
    "    # overriding abstract method\n",
    "    def noofsides(self):\n",
    "        print(\"Triangle: I have 3 sides\")\n",
    " \n",
    "class Pentagon(Polygon): #subclass\n",
    " \n",
    "    # overriding abstract method\n",
    "    def noofsides(self):\n",
    "        print(\"Pentagon: I have 5 sides\")\n",
    " \n",
    "class Hexagon(Polygon): #subclass\n",
    " \n",
    "    # overriding abstract method\n",
    "    def noofsides(self):\n",
    "        print(\"Hexagon: I have 6 sides\")\n",
    " \n",
    "class Quadrilateral(Polygon): #subclass\n",
    " \n",
    "    # overriding abstract method\n",
    "    def noofsides(self):\n",
    "        print(\"Quadrilateral: I have 4 sides\")\n",
    " \n",
    "# Driver code\n",
    "# Creating the objects to call the abstract method.\n",
    "R = Triangle()\n",
    "R.noofsides()\n",
    " \n",
    "K = Quadrilateral()\n",
    "K.noofsides()\n",
    " \n",
    "R = Pentagon()\n",
    "R.noofsides()\n",
    " \n",
    "K = Hexagon()\n",
    "K.noofsides()"
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
