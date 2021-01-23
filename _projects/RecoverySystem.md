---
title: "A Legged Robot Recovery System"
excerpt: "Project to design an active assist and recovery system for a planar bipedal robot. <br/><img src='/images/ramonePreview.jpg'>"
collection: portfolio
---

This work aimed to create a vertical support system for the robot RAMone which was [presented at AIM 2016](https://ieeexplore.ieee.org/document/7576893). The system working is shown in the video below.



This system is a series elastic, unidirectional cable system that actuates the sliders that constrain RAMone to be planar. A pictorial diagram of the system is shown below.

<img src='/images/recoverySystem.png'>

The configuration of pulleys allow the middle section to move left and right freely, but it cannot lower unless the motor and spool unwinds to let out cable. This system is series elastic due to the spring on the right through which the cable is connected to the frame. Additionally we use a hanging mass (Mh) to allow the system to “go slack” without actually having the cable go slack. If the motor lets out more cable than is required, the hanging mass is lowered.

This system was designed to be able to operate in three different ways.

__1. Shadowing Mode__

In this mode the system will apply very low forces on the robot. This is for normal operation where the system should not be intervening. It is called shadowing mode because the system must be ready to act quickly if intervention is necessary. Conceptually this is similar to a parent holding their hands up, ready to catch a toddler as they try to take a step.

We use a simple proportional controller with feedforward velocity to shadow the robot. The control law we used is

<img src='/images/shadowcontrol.png' height="50%" width="50%">

where y dot motor is the commanded spool velocity, d is the desired gap, yr and y dot r are the position and velocity of the robot and yp is the current position of the spool.

__2. Support Mode__

In this mode the system applies a supportive vertical force to assist the robot. This is similar to a parent helping support the weight of a child as they learn to walk.

We use a relative simple control method for this system. We command a velocity to a low level controller according to the following control law.

<img src='/images/forcecontrol.png' height="50%" width="50%">

We feed forward the vertical velocity of the robot measured from the linear encoder on the slider, then we use porportional feedback between the desired vertical force and the filtered measured force from the load cell.

__3. Recovery Mode__

In this mode the robot has started to fall and needs assistance to avoid damage. When a fall is detected the system should quickly lift the robot up to prevent the legs or body from striking the ground. We generate a trajectory to lift the robot up to a safe height using a saturated second order setpoint filter, shown below. When we detect a fall, we initialize the setpoint filter's internal state to match the current measured position and velocity of the robot. Then we set the input, goal position, to be a predefined, constant safe holding height. The saturations are required because we want to ensure limit the maxium speed and acceleration of the robot as it is lifted.

<img src='/images/setpointfilter.png'>

This filter outputs a velocity and a position which we servo on using a porportional plus feedforward controller.

<img src='/images/recoveryControl.png' height="50%" width="50%">

The plot below shows data from a failure and catch.

<img src='/images/recoveryplot.png'>






