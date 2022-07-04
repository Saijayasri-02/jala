{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b2500da5",
   "metadata": {},
   "outputs": [],
   "source": [
    "class A():  \n",
    "    def display(dp):\n",
    "        print(\"Display Inside class A \")\n",
    " # class A show method    \n",
    "    def show(self):\n",
    "        print(\"Show Inside class A\")\n",
    "    \n",
    "# Inherited or Sub class (Note A in bracket) \n",
    "class B (A): \n",
    "    def print(pt):\n",
    "        print(\"Print Inside class B\")    \n",
    "    # class B show method\n",
    "    def show(self):\n",
    "        print(\"Show Inside class B\")\n",
    "    \n",
    "# Inherited or Sub class (Note B in bracket) \n",
    "class C (B): \n",
    "          \n",
    "    # class C show method\n",
    "    def show(self):\n",
    "        print(\"Show Inside class C \")         \n",
    "    \n",
    "# Driver code \n",
    "s = A()\n",
    "s.display()\n",
    "k= B()\n",
    "k.print()\n",
    "g = C()   \n",
    "g.show()"
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
