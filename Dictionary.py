{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "09ba2eac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dictionary with each item as a pair: {1: 'Kashish', 2: 'Kritika', 3: 'Aastha', 4: 'Vaishali', 5: 'Muskan'}\n",
      "\n",
      " Dictionary with new item added: {1: 'Kashish', 2: 'Kritika', 3: 'Aastha', 4: 'Vaishali', 5: 'Muskan', 6: 'Nitya'}\n",
      "\n",
      " Dictionary with updated values: {1: 'Kashish', 2: 'Kritika', 3: 'Navdisha', 4: 'Vaishali', 5: 'Muskan', 6: 'Nitya'}\n",
      "\n",
      " Accessing one value in Dictionary: Kashish\n",
      "\n",
      " Delete a value from a Dictionary: {1: 'Kashish', 2: 'Kritika', 3: 'Navdisha', 4: 'Vaishali', 5: 'Muskan'}\n",
      "\n",
      " Nested loop Dictionary: {1: 'Kashish', 2: 'Kritika', 3: {'Age': 18, 'Branch': 'CSE', 'Year': 'Third Year'}}\n",
      "\n",
      " Accessing an element of a Nested Dictionary: Kritika\n"
     ]
    }
   ],
   "source": [
    "#Creating dictionary\n",
    "Dict = dict([(1,'Kashish'), (2,'Kritika'), (3,'Aastha'), (4,'Vaishali'), (5,'Muskan')])\n",
    "print(\"Dictionary with each item as a pair:\",Dict) #printing dictionary\n",
    "\n",
    "#adding element in dictionary\n",
    "Dict[6] = 'Nitya'\n",
    "print(\"\\n Dictionary with new item added:\",Dict)\n",
    "\n",
    "#updating values in dictionary\n",
    "Dict[3] = 'Navdisha'\n",
    "print(\"\\n Dictionary with updated values:\",Dict)\n",
    "\n",
    "print(\"\\n Accessing one value in Dictionary:\",Dict[1])\n",
    "\n",
    "#deleting value from drictionary\n",
    "del Dict[6]\n",
    "print(\"\\n Delete a value from a Dictionary:\",Dict)\n",
    "\n",
    "#creating a nested dictionary\n",
    "Dict1 = {1: 'Kashish', 2: 'Kritika',\n",
    "        3:{'Age' : 18, 'Branch' : 'CSE', 'Year' : 'Third Year'}}\n",
    "print(\"\\n Nested loop Dictionary:\",Dict1)\n",
    "\n",
    "print(\"\\n Accessing an element of a Nested Dictionary:\",Dict1[2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "62b25655",
   "metadata": {},
   "outputs": [],
   "source": []
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
