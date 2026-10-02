"""
Luz encendida: Una lámpara (L) se enciende si el interruptor A o el interruptor B están activados.
Acceso permitido: Entras a la sala (E) si tienes la llave (A) y conoces la contraseña (B).
Alarma de seguridad: La alarma (A) suena si el sensor de movimiento (M) se activa, pero solo si el
sistema no está en modo mantenimiento (not Mnt).
Selección de personal: Un candidato es preseleccionado (P) si tiene título universitario (T) o tiene más de 5 años de experiencia (E).
Compra aprobada: El pago se procesa (P) si la tarjeta tiene fondos (F) y el PIN es correcto (C).
Apagado automático: El motor se detiene (D) si la temperatura es alta (T) o si se presiona el botón de emergencia (E).#
Modo silencioso: El teléfono no suena (not S) si está activado el modo reunión (R) o el modo avión (A).
Descuento aplicado: Tienes descuento (D) si eres estudiante (E) y además es día laborable (L).

Si A AND B ---> E
Si M AND NOT Mnt ---> A
Si T OR E ---> P
Si F AND C ---> P
Si T OR E ---> D
Si R OR A ---> NOT S
Si E AND L ---> D

Riego automático: El jardín se riega (R) si la tierra está seca (S) y no está lloviendo (not LL).
Viaje en avión: Puedes subir al avión (V) si tienes el billete (B) y presentas el pasaporte (P) o
el DNI (D).
Alerta de motor: Se enciende la luz de fallo (F) si la presión es baja (P) o si el aceite es
bajo (A) pero el motor está encendido (M).
Beca de estudios: Te dan la beca (B) si tus ingresos son bajos (I) y cumple una de estas dos:
buen expediente (E) o residencia lejana (R).
Ventana segura: La alarma se activa (A) si la ventana está abierta (V) y no es de día (not D).
Acceso al club: Entras (E) si eres socio vip (V), o si eres mayor de edad (M) y vienes acompañado (A).
Sensor de inundación: La bomba se activa (B) si el nivel de agua es alto (A) y la bomba no
está averiada (not Av).
Cancelación de evento: El concierto se cancela (C) si llueve (LL) y el recinto no tiene techo (not T).

Si S AND NOT LL ---> R
Si B AND (P OR D) ---> V
Si P OR (A AND M) ---> F
Si I AND (E OR R) ---> B
Si V AND NOT D ---> A
Si V OR (M AND A) ---> E
Si A AND NOT Av ---> B
Si LL AND NOT T ---> C

Sistema de calefacción: La calefacción se enciende (C) si hace frío (F) y estás en casa (H), o
si hace frío (F) y tienes la programación automática activada (P).
Apertura de caja fuerte: La caja se abre (C) si se introducen las llaves de los dos
administradores (A y B), o si la abre el superusuario (S) siempre que no esté el sistema bloqueado (not B).
Aprobado de asignatura: Apruebas (A) si apruebas el examen final (F), o si
entregas todos los proyectos (P) y la nota de clase es alta (C) pero no has faltado a
las prácticas (not Falt).
Control de crucero: El coche mantiene la velocidad (CC) si el sistema está encendido (E),
el conductor no está pisando el freno (not F) y no está pisando el embrague (not Em).
Compra online con cupón: El carrito acepta el cupón (Cup) si el usuario es nuevo (N) y la
compra supera los 50€ (C), o si el usuario es antiguo (A) pero tiene una cuenta premium (P).
Ascensor en movimiento: El ascensor se mueve (M) si las puertas están cerradas (C) y se da
una de estas situaciones: se ha pulsado un botón interno (I) o hay una llamada externa (E).

Si F AND (H OR P) ---> C
Si (A AND B) OR (S AND NOT B) ---> C
Si F OR (P AND C AND NOT Falt) --> A
Si E AND NOT F AND NOT Em ---> CC
Si (N AND C) OR (A AND P) ---> Cup
Si C AND (I OR E) ---> M

Climatización inteligente: El aire acondicionado se enciende (AA) si la temperatura supera
los 26°C (T) y hay gente en la habitación (P), a menos que la ventana esté abierta (V)
(si la ventana está abierta, nunca se enciende).
Sistema de votación secreta: Un proyecto es aprobado (P) si votan a favor al menos dos
de los tres miembros del comité (A, B, C).
Validar contraseña nueva: La contraseña es válida (V) si tiene más de 8 caracteres (C) y
al menos un número (N), o si tiene más de 8 caracteres (C) y al menos un símbolo (S), siempre
y cuando no contenga el nombre del usuario (not U).

Si T AND P AND NOT V ---> AA
Si (A AND B) OR (A AND C) OR (B AND C) ---> P
Si ((C AND N) OR (C AND S)) AND NOT U ---> V
"""
print(0 % 4 == 0)