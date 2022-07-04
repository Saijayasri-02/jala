{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "94110f1a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# super class\n",
    "class Super:\n",
    "     \n",
    "     # public data member\n",
    "     var1 = None\n",
    " \n",
    "     # protected data member\n",
    "     _var2 = None\n",
    "      \n",
    "     # private data member\n",
    "     __var3 = None\n",
    "     \n",
    "     # constructor\n",
    "     def __init__(self, var1, var2, var3): \n",
    "          self.var1 = var1\n",
    "          self._var2 = var2\n",
    "          self.__var3 = var3\n",
    "     \n",
    "    # public member function  \n",
    "     def displayPublicMembers(self):\n",
    "  \n",
    "          # accessing public data members\n",
    "          print(\"Public Data Member: \", self.var1)\n",
    "        \n",
    "     # protected member function  \n",
    "     def _displayProtectedMembers(self):\n",
    "  \n",
    "          # accessing protected data members\n",
    "          print(\"Protected Data Member: \", self._var2)\n",
    "      \n",
    "     # private member function  \n",
    "     def __displayPrivateMembers(self):\n",
    "  \n",
    "          # accessing private data members\n",
    "          print(\"Private Data Member: \", self.__var3)\n",
    " \n",
    "     # public member function\n",
    "     def accessPrivateMembers(self):    \n",
    "           \n",
    "          # accessing private member function\n",
    "          self.__displayPrivateMembers()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6e80f890",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "179587ee",
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
