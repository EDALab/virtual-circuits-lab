# virtual-circuits-lab
The **backend** of the web-based virtual circuits lab.  
It is built using `Python` with `Flask`.  
Please refer to our **frontend** at [circuit-simulator-frontend](https://github.com/YukaiZhang2019/circuit-simulator-frontend).

## To Install Required Packages
#### For PySpice Only
1. PyCharm:  
    *settings -> project -> Python Interpreter:*  
        *install:* `PySpice`
2. Run the following on command line:
```
pyspice-post-installation --install-ngspice-dll
pyspice-post-installation --check-install
```

## To Run
Run `app.py`.  
For other steps, please refer to the instructions in our [frontend repository](https://github.com/YukaiZhang2019/circuit-simulator-frontend).

## To Test
Use [Postman](https://www.postman.com/) to send HTTP Requests and receive HTTP Responses.

## PySpice Documentation
Please refer to [PySpice](https://github.com/FabriceSalvaire/PySpice).

## Acknowledgement
Aside from the SPICE functions, this backend code structure is built based on a template we studied in a public online course on Udemy, provided by Jose Salvatierra of Teclado
The course can be found here:  
[REST APIs with Flask and Python](https://www.udemy.com/share/1026WUAEAaeFlTQnkF/)  
[Advanced REST APIs with Flask and Python](https://www.udemy.com/share/101sjYAEAaeFlTQnkF/)

---

## Note for Programmers
All files marked as `template` is for setting up the *authorization levels* (built upon the template from the previous section (i.e., Acknowledgement).  
For circuit simulation, please refer to `simulate.py`, for the web application, please refer to `app.py`.

### Implemented Circuit Elements
1. DC Voltage Source
2. DC Current Source
3. Sinusoidal Voltage Source
4. Sinusoidal Current Source
5. Resistor
6. Capacitor
7. Inductor
8. Voltmeter
9. Ammeter
10. Diode
11. BJT (NPN, PNP)
12. MOSFET (NMOS, PMOS)
