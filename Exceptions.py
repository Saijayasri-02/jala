{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e8440882",
   "metadata": {},
   "outputs": [],
   "source": [
    "a = [1, 2, 3]\n",
    "try:\n",
    "    print (\"Second element = \",a[1])\n",
    " \n",
    "    # Throws error since there are only 3 elements in array\n",
    "    print (\"Fourth element = \",a[3])\n",
    "    \n",
    "except:\n",
    "    print (\"An error occurred\")\n",
    "\n",
    "print()\n",
    "\n",
    "b = [3,2,1]\n",
    "try:\n",
    "    a == b\n",
    "except:\n",
    "    print(\"They are not equal\")\n",
    "else:\n",
    "    print(\"Both Equal\") \n",
    "\n",
    "print()\n",
    "\n",
    "try:\n",
    "    k = 5/0\n",
    "    print(k)\n",
    "except ZeroDivisionError:\n",
    "    print(\"Can't divide by zero\")\n",
    "finally:\n",
    "    print('This is always executed') "
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
