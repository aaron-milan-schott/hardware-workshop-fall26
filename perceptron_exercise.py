"""
NEURON EXERCISE: build a perceptron, then use it to move real hardware
Hardware: Arduino Uno, hobby servo, LED (already wired for you)

A perceptron is the simplest artificial neuron. It takes numbers in,
multiplies each one by a weight, adds them up with a bias, and fires (1)
if the total is above zero or stays quiet (0) if it is not:

    total  = (w1 * x1) + (w2 * x2) + bias
    output = 1 if total > 0, otherwise 0

It learns by guessing, checking its guess against the right answer, and
nudging its weights whenever it is wrong.

In this exercise you will teach your neuron to behave like an AND gate (it
should only fire when BOTH inputs are 1). Then you will send its decisions
over the USB cable to your Arduino so the servo and LED react.

Fill in every blank marked with ____
Do not change anything else.

Run it with:   python3 perceptron.py
If Python complains, read the LAST line of the error first. It tells you
what went wrong. The lines above it only tell you where.
"""


# ---- STEP 1 -------------------------------------------------------------
# Python does not know how to do fast maths on lists of numbers, or how to
# talk over a USB cable, out of the box. Libraries add those abilities.
#
# numpy does the maths. By convention it is imported under the short name
# np, so you can type np.something instead of numpy.something.
#
# pyserial does the USB talking. The name you import is the word for
# sending data one piece after another: serial.
import numpy as ____
import ____
import time
import os


class Perceptron:

    def __init__(self, n_features, lr=0.1):
        # ---- STEP 2 -------------------------------------------------------
        # A perceptron has one weight for every input. They all start at zero.
        # np.zeros(n) makes a list of n zeros.
        #
        # It also has a bias that starts at 0.0, and a learning rate that
        # says how big each nudge is. The learning rate arrives as the
        # argument named lr. Store it, do not retype the number.
        self.w = np.____(n_features)
        self.b = ____
        self.lr = ____

    def predict(self, x):
        # ---- STEP 3 -------------------------------------------------------
        # np.dot multiplies matching items from two lists and adds up the
        # results: (w1 * x1) + (w2 * x2). Add the bias to that total.
        #
        # Fire (1) if the total is greater than zero. Otherwise stay quiet (0).
        return 1 if np.____(self.w, x) + self.b > ____ else 0

    def fit(self, X, y, epochs=10):
        # ---- STEP 4 -------------------------------------------------------
        # An epoch is one full pass through every training example.
        # Repeat the whole pass as many times as the argument `epochs` says.
        for _ in range(____):

            # zip pairs up each row of inputs (xi) with its right answer (yi).
            for xi, yi in zip(X, y):

                # error = right answer - the neuron's guess.
                # It is 0 when the neuron is correct, and +1 or -1 when wrong.
                err = ____ - self.predict(xi)

                # Nudge every weight to fix the mistake. The nudge is scaled by
                # the learning rate, the error, and how big the input was.
                self.w += self.lr * ____ * xi

                # The bias gets the same nudge, but without the input.
                self.b += self.lr * ____


# ---- STEP 5 -------------------------------------------------------------
# Training data for an AND gate. Each row of X is one pair of inputs.
# y holds the right answer for each row, in the same order.
# AND only outputs 1 when BOTH inputs are 1. Fill in the four answers.
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([____, ____, ____, ____])


# ---- STEP 6 -------------------------------------------------------------
# Create a perceptron with one weight per input. How many numbers are in
# each row of X?
p = Perceptron(____)
p.fit(X, y)

# This line should print  [0, 0, 0, 1]  before you go any further.
print("Neuron says:", [p.predict(x) for x in X])


# =========================================================================
# CONNECTING PYTHON TO THE ARDUINO
#
# The USB cable carries a stream of bytes. Your Arduino sketch is listening
# for the character 1 (the neuron fired) or the character 0 (it did not),
# and it ignores the newline character at the end of each message.
# =========================================================================

# Where your Arduino is connected. Do not change this line.
PORT = os.environ.get("ARDUINO_PORT", "/dev/ttyACM0")

# ---- STEP 7 -------------------------------------------------------------
# Both sides of a serial connection must agree on the speed, or they hear
# garbage. This must match the number in Serial.begin() in your Arduino
# sketch.
BAUD = ____

ser = serial.Serial(PORT, BAUD)

# Opening the port restarts the Arduino, just like pressing its reset
# button. Give it a moment to boot, or the first message is lost.
# time.sleep() counts in SECONDS (not milliseconds like Arduino delay()).
# Wait 2 seconds.
time.sleep(____)


# ---- STEP 8 -------------------------------------------------------------
# Run every input through the trained neuron and send its decision to the
# Arduino.
for xi in X:
    result = p.predict(xi)
    print("Inputs", xi, "-> neuron output", result)

    # A serial connection sends bytes, not numbers. Turn the neuron's result
    # into text, add a newline to mark the end of the message, then encode
    # the text into bytes with the .encode() style of method.
    message = str(____) + "\n"
    ser.write(message.____())

    # Hold for 2 seconds so you have time to watch the servo and LED.
    time.sleep(____)

# Always close the port when you are finished. Your Arduino sketch cannot be
# uploaded while Python is still holding the port open.
ser.____()


# ---- WHEN IT WORKS, TRY THESE -------------------------------------------
#
#  A. Change y to teach the neuron an OR gate: 0, 1, 1, 1. Which inputs
#     move the servo now?
#
#  B. Change y to an XOR gate: 0, 1, 1, 0. What does the neuron say? Try
#     more epochs. Can a single perceptron ever learn XOR? (Sketch the four
#     points on paper and try to separate the 1s from the 0s with one
#     straight line.)
#
#  C. Train with epochs=1, then 2, then 5, then 10. How many passes does the
#     neuron need before it is always right? Then try lr=0.01 and lr=1. Did
#     it change anything? Can you work out why?
#
#  D. After training, print p.w and p.b. Work out by hand what the neuron
#     calculates for the input [1, 1]. Does it match?
#
#  E. Replace the for loop with a loop that asks you to type the two inputs
#     with input(), runs them through the neuron, and sends the result.


# ---- IF SOMETHING GOES WRONG --------------------------------------------
#
#  ModuleNotFoundError: No module named 'serial'
#      pyserial is not installed for your user. Ask the instructor.
#
#  FileNotFoundError or SerialException when opening the port
#      The port path is wrong, or the Arduino is not plugged in.
#
#  PermissionError on the port
#      Your user is not allowed to use that port. Check you are logged in
#      as your own group, then ask the instructor.
#
#  "device or resource busy" when opening the port
#      Another program is holding the port. Close any other copy of this
#      script. Only one program can use the port at a time.
#
#  Neuron says [0, 0, 0, 0] or something wrong
#      Check your y values, and check that fit() uses the error in both
#      weight and bias updates.
#
#  The servo does nothing at all
#      Check the baud rate matches your Arduino sketch, and that the sketch
#      is uploaded and listening for the characters 1 and 0.
#
#  The first message seems to be ignored
#      Opening the port restarts the Arduino. Wait longer after opening it.
#
#  TypeError mentioning bytes
#      ser.write() only accepts bytes. Encode your text first.
#
#  IndentationError
#      Python uses the spaces at the start of a line to know what belongs
#      inside what. Do not add or remove them.
