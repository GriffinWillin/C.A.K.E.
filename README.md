Project Summary

The C.A.K.E. is an automatic, programmable device meant for precise, rapid, and safe
slicing of pies, cakes, and other flat, round desserts. The device is a small box into which a
dessert is inserted. It then uses a rotating, mechanically lowered blade assembly to slice the
dessert into 2, 4, 6, or 8 slices; two blades are lowered, completing a slice, followed by a
retraction of the blade. It then rotates by a specified amount and completes another cut,
repeating until the dessert has been diced into an even number of slices. The number of slices,
cut depth, and cut speed are all controllable via a touchscreen interface on an LCD screen built
into the device. A physical emergency stop switch is also present.

GPIO

The GPIO involved in the project would include a motor, another motor or servo of some
sort, a low-power laser used for dessert alignment, the touchscreen, a speaker, and an
emergency stop button. Encoders, magnetic sensors which monitor motor position, could be
used on the blade actuation motor, allowing the speed and depth of each cut to be precisely
controlled. A servo could be used to control the rotation of the blade.
A small pointing laser, centered in the machine, can be turned on during insertion to help
the user center the desert in the cutting area. To ensure no hands are in the cutting area during
operation, the C.A.K.E. cannot be activated while this laser is on. To further improve safety, a
speaker can be implemented and used to emit a low tone, to alert those around the machine
when it is in operation.

Importantly a physical emergency stop is also present; it overrides the computer control
and automatically retracts the blade fully, independently of the primary operation of the device.
While the “E-Stop” is engaged, the device cannot be operated.

GUI

The operating GUI is rendered via Python on the LCD touchscreen; buttons are
designed to be large and colored for easy operation, with sensible arrangements and images to
maximize clarity. The user can control the number of cuts, the operating speed, and the depth of
each cut, as well as toggle the alignment laser. A button is present for starting the cut; once
operation has begun, the start button turns into a “stop” button, which will simply stop the cut
and fully retract the blade. There is also a redundant emergency stop independent of the
physical one