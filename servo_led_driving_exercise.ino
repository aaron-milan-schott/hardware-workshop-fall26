/*
 * NEURON OUTPUT EXERCISE
 * Hardware: Arduino Uno, hobby servo, LED
 *
 * In this exercise your Python script is the "neuron". Each time it makes a
 * decision, it sends one character over the USB cable:
 *
 *     1  = the neuron fired
 *     0  = the neuron did not fire
 *
 * Your Arduino listens for that character and reacts with a servo and an LED.
 *
 * WIRING (do this before you touch the code):
 *   Servo ground wire -> GND on the Arduino
 *   Servo power wire  -> 5V  on the Arduino
 *   Servo signal wire -> pin 3   (the wire that is not power or ground)
 *   LED long leg      -> pin 5 through a resistor
 *   LED short leg     -> GND
 *
 * Fill in every blank marked with ____
 * Do not change anything else.
 *
 * When you are done, compile the sketch before you upload it.
 * If the compiler complains, read the FIRST error only - the rest are
 * usually just knock-on effects of that one.
 */


/* ---- STEP 1 -------------------------------------------------------------
 * Arduino does not know how to talk to a servo out of the box. The timing
 * pulses a servo needs are fiddly, so someone already wrote that code for
 * you and packaged it as a library.
 *
 * Bring that library into your sketch. The library's name is the same as
 * the thing it controls, with a capital letter.
 */
#include <____.h>


/* ---- STEP 2 -------------------------------------------------------------
 * Create a servo object. Think of this like creating a variable, except
 * the "type" is Servo and the value is a physical motor.
 *
 * The type goes first, then a name you pick. Name it something you will
 * not mind typing twenty times.
 */
Servo ____;


/* ---- STEP 3 -------------------------------------------------------------
 * Store each pin number in a named constant instead of typing the raw
 * number all over the sketch. Check the wiring comment at the top of this
 * file for which pin is which.
 *
 * `const` means "this never changes." The compiler will stop you if you
 * try to change it later, which is the point.
 */
const int SERVO_PIN = ____;
const int LED_PIN   = ____;


void setup() {
  /* ---- STEP 4 -----------------------------------------------------------
   * setup() runs exactly once, when the board powers up.
   *
   * Tell your servo object which pin it lives on. The function you want is
   * called attach(), and you call it ON your servo object using a dot:
   *
   *     objectName.functionName(argument);
   *
   * Pass it the constant you defined in step 3 - not the bare number.
   */
  ____.attach(____);


  /* ---- STEP 5 -----------------------------------------------------------
   * A pin can either send voltage out or listen for voltage coming in.
   * Your LED needs the pin to send voltage OUT. Set the mode of the LED pin
   * with pinMode(). The mode you want is spelled in capital letters.
   *
   * Then open the serial connection to the Python script. Both sides must
   * agree on the speed. The Python script talks at 9600.
   */
  pinMode(____, ____);
  Serial.begin(____);


  /* ---- STEP 6 -----------------------------------------------------------
   * Send the servo to a known starting position so every run begins the
   * same way. Use 0 degrees.
   *
   * The function that commands a position is write(). It takes an angle
   * from 0 to 180.
   *
   * Then make sure the LED starts switched off. digitalWrite() takes a pin
   * and either HIGH (on) or LOW (off).
   */
  ____.____(____);
  digitalWrite(____, ____);

  /* Give the servo time to physically get there before loop() starts.
   * It cannot teleport. A typical hobby servo covers 60 degrees in about
   * 0.15 seconds. How many milliseconds does a full 180 degree move need?
   * Round up. */
  delay(____);
}


void loop() {
  /* ---- STEP 7 -----------------------------------------------------------
   * loop() runs over and over, forever, as long as the board has power.
   *
   * Characters from Python wait in a small buffer until you read them.
   * Serial.available() tells you how many characters are waiting. Only
   * read when there is at least one.
   *
   * Pick the function that reports how many characters are waiting, and
   * the function that reads one character out of the buffer.
   */
  if (Serial.____() > 0) {
    char value = Serial.____();


    /* ---- STEP 8 ---------------------------------------------------------
     * Python sends the CHARACTER 1, not the number 1. A single character
     * goes in single quotes, like '1'. Comparing two things uses TWO equals
     * signs: ==
     *
     * If the neuron fired ('1'), move the servo to the far end of its
     * travel (180) and turn the LED on.
     */
    if (value == '____') {
      ____.write(____);
      digitalWrite(____, ____);
    }


    /* ---- STEP 9 ---------------------------------------------------------
     * If the neuron did not fire ('0'), send the servo back to 0 and turn
     * the LED off.
     *
     * Anything else that arrives, including the newline character Python
     * adds to the end of every message, matches neither check and is
     * ignored. That is what you want.
     */
    if (value == '____') {
      ____.write(____);
      digitalWrite(____, ____);
    }
  }
}


/* ---- WHEN IT WORKS, TRY THESE -------------------------------------------
 *
 *  A. Pin 5 can do more than on and off. Replace digitalWrite() on the LED
 *     with analogWrite(LED_PIN, 128). What changes? What does 255 look
 *     like? What does 20 look like?
 *
 *  B. Instead of snapping to 180, make the servo sweep there smoothly with
 *     a for loop that counts angle up from 0 to 180, calling write() and
 *     delay(15) on each pass.
 *
 *  C. Change the Python script so it sends a different character. What
 *     does your Arduino do when it receives something it does not
 *     recognize?
 *
 *  D. Echo what you received back to Python with Serial.println(value);
 *     and read it on the Python side.
 */


/* ---- IF SOMETHING GOES WRONG --------------------------------------------
 *
 *  Upload fails with "port busy" or similar
 *      Only one program can use the serial port at a time. Stop the Python
 *      script, then upload again.
 *
 *  Servo buzzes but does not move
 *      It is being asked to go somewhere it cannot reach, or it is
 *      straining. Check your angle is between 0 and 180.
 *
 *  Servo twitches and the board resets
 *      The servo is drawing more current than USB can supply. Take any
 *      load off it.
 *
 *  LED never lights
 *      Check the long leg goes toward pin 5 and the short leg toward GND.
 *      An LED only works one way round.
 *
 *  Nothing happens at all
 *      Check the servo signal wire is in the right pin, and that its ground
 *      wire goes to GND. A servo with no ground connection looks exactly
 *      like a dead servo.
 *
 *  Nothing happens on the first message only
 *      Opening the serial port restarts the Arduino. Messages sent in the
 *      first second or two are lost. Wait a moment after connecting.
 *
 *  "expected ';' before..."
 *      You are missing a semicolon, and it is on the line ABOVE the one
 *      the compiler is pointing at.
 */
