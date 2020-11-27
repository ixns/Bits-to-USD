import requests
import json
from time import sleep
import tkinter as tk
window = tk.Tk()
window.title("Bits to USD Converter")
window.minsize(285,100)
                    

def onReturn(*args):
    try:
        name = entry.get()
        bitsInput = float(name)
    except:
        windowerror1 = tk.Tk()
        windowerror1.title("Result")
        windowerror1.minsize(20,20)
        w = tk.Label(windowerror1, text="Error")
        w.pack()
    else:
        name = float(entry.get())
        formattedName = '{:,.2f}'.format(name)
        bitsInput = float(name)
        btcPrice = float(getBitcoinPrice())
        btcAmount = bitsInput / 1000000
        btcUSDno = float(btcAmount * btcPrice)
        btcUSD = float(btcUSDno)
        formattedUSD = '{:,.2f}'.format(round(btcUSD,2))
        window1 = tk.Tk()
        window1.title("Result")
        window1.minsize(20,20)
        z = tk.Label(window1, text=(formattedName, "bits =","$",
                                    formattedUSD, "USD"))
        z.pack()


def onReturnUSD(*args):
  
     try:
        nameUSD = USDentry.get()
        USDinput = float(nameUSD)
     except:
        windowerror2 = tk.Tk()
        windowerror2.title("Result")
        windowerror2.minsize(20,20)
        w = tk.Label(windowerror2, text="Error")
        w.pack()
     else:
        nameUSD = float(USDentry.get())
        formattedNameUSD = '{:,.2f}'.format(nameUSD)
        USDinput = float(nameUSD)
        btcPrice = float(getBitcoinPrice())
        btcChunk = USDinput / btcPrice
        bitsAmount = float(btcChunk * 1000000)
        formattedBits = '{:,.2f}'.format(round(bitsAmount,2))
        window2 = tk.Tk()
        window2.title("Result")
        window2.minsize(20,20)
        
        x = tk.Label(window2, text=("$",formattedNameUSD, "USD =", formattedBits, "bits"))
        x.pack()



def getBitcoinPrice():
    URL = "https://www.bitstamp.net/api/ticker/"
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)["last"])
        return priceFloat
    except requests.ConnectionError:
        print("Error querying Bitstamp API")

def getFormattedBitcoinPrice():
    URL = "https://www.bitstamp.net/api/ticker/"
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)["last"])
        formattedPrice = '{:,.2f}'.format(priceFloat)
        return formattedPrice
    except requests.ConnectionError:
        print("Error querying Bitstamp API")




label = tk.Label(text="Bits")
entry = tk.Entry()
entry.bind("<Return>", onReturn)
label.pack()
entry.pack()


USDlabel = tk.Label(text="USD $")
USDentry = tk.Entry()
USDentry.bind("<Return>", onReturnUSD)
USDlabel.pack()
USDentry.pack()
c = tk.Label(window, text=("BTC Price: $", getFormattedBitcoinPrice()))
c.pack()
q = tk.Label(window, text=("Know when to stop. Set a Goal and stick to it."))
q.pack()


###############
window.mainloop()
###############
