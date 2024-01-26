"""
Program: InvestmentGui.py
Chapter 8 (Page 251)
1/18/2024

**NOTE: The module breezypythongui.py
MUST be in the same directory as this
file for the app to run correctly.

Gui-based investment app.
"""
from breezypythongui import EasyFrame
from tkinter.font import Font

# Other imports go here.

# Class header (class name will change from project to project.)
class TextAreaDemo(EasyFrame):
	#Definition of our classes' constructor method
	def __init__(self):
		# Call to the EasyFrame class constructor.
		EasyFrame.__init__(self, title = "Salary Calculator", width = 600, height = 600, background = "yellow")
		# Create a variable from the Font class.
		myFont = Font(family = "Verdana", size = 20, slant = "italic")
		myFont1 = Font(family = "Arial", size = 20, slant = "italic")

		self.addLabel(text = "Initial Amount", row = 0, column = 0, font = myFont, background = "skyblue")
		self.addLabel(text = "Number of Years", row = 1, column = 0, font = myFont, background = "palegoldenrod")
		self.addLabel(text = "Interest Rate in %", row = 2, column = 0, font = myFont, background = "Aqua")
		self.amount = self.addFloatField(value = 0.0, row = 0, column = 1,)
		self.period = self.addIntegerField(value = 0, row = 1, column = 1, width = 20)
		self.rate = self.addFloatField(value = 0, row = 2, column = 1)
		self.compute = self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, command = self.compute)
		self.outputArea = self.addTextArea(text = "", row = 4, column = 0, columnspan = 2, width = 56, height = 20)
#		self.outputField = self.addTextField(text = "", row = 4, column = 0, state = "readonly")	
	# Definition of the compute function, which is the event handler.
	def compute(self):
			""" Computes the investment schedule based on the inputs and outputs to the text area widget in tabular format."""
			# Obtain and validate the inputs.
			startBalance = self.amount.getNumber()
			years = self.period.getNumber()
			rate = self.rate.getNumber() / 100
			if startBalance == 0 or years == 0 or rate == 0:
				return

			# Set the header for the table.
			result = "%4s%18s%10s%16s\n" % ("Year", "Starting Balance", "Interest", "Ending Balance")

			# Compute and append the results for each year.

			totalInterest = 0.0
			for year in range(1, years + 1):
				interest = startBalance * rate
				endBalance = startBalance + interest
				result += "%4d%18.2f%10.2f%16.2f\n" % (year, startBalance, interest, endBalance)
				startBalance = endBalance
				totalInterest += interest

			# Append the totals for the investment period.
			result += "Ending balance: $%0.2f\n" % endBalance
			result += "Total interest earned: %0.2f\n" % totalInterest

			# Output the result variable while keepin read-only status
			self.outputArea["state"] = "normal"
			self.outputArea.setText(result)
			self.outputArea["state"] = "disabled"


# Global definition of the main() method.
def main():
	# Instantiate an object from the class into mainLoop()
	TextAreaDemo().mainloop()

# Global call to main() for program entry.
if __name__ == '__main__':
	main()



