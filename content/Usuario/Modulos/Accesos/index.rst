.. _doc-accesos:

==============
Módulo Accesos
==============

El **módulo Accesos** está diseñado para gestionar y controlar el acceso de personas a una ubicación específica. 
Este módulo es esencial para garantizar la seguridad y la organización dentro de cualquier instalación, permitiendo a los usuarios autorizados supervisar y administrar las entradas y salidas, así como otras funciones relacionadas con la seguridad.

El propósito principal del módulo de Accesos es proporcionar un control riguroso sobre quién puede ingresar a una instalación, cuándo y con qué permisos. Este módulo es utilizado principalmente por el personal de seguridad, recepcionistas y recursos humanos para crear pases de entrada, gestionar perfiles de visitantes y empleados, y registrar incidencias y fallos. Además, se enfoca en:

- **Control de entradas y salidas**: Asegura que solo personas autorizadas ingresen a las áreas designadas.
- **Gestión de permisos**: Asigna y controla permisos específicos necesarios para ciertos perfiles de visitantes y empleados.
- **Registro de incidencias y fallos**: Mantiene un registro detallado de cualquier incidente o fallo reportado.
- **Concesión y control de equipos**: Facilita el seguimiento de equipos y objetos dentro de la instalación.

El módulo de Accesos está compuesto por varias formas y catálogos que se interrelacionan para ofrecer una funcionalidad completa y detallada. 
A continuación, se presenta una lista de los componentes del módulo, organizados en el orden lógico de su utilización:

1. **Notas**
2. **Checkin - Checkout Casetas**
3. **Definición de Permisos**
4. **Configuración de Perfiles**
5. **Visita Autorizada**
6. **Carga de Permisos de Visitantes**
7. **Pase de Entrada**
8. **Bitácora de Entradas y Salidas**
9. **Bitácora de Gafetes y Lockers**
10. **Bitácora de Incidencias**
11. **Bitácora de Fallas**
12. **Concesión de Activos Único**
13. **Concesión de Activos Múltiple**
14. **Bitácora de Artículos Perdidos**
15. **Configuración de Recorridos**
16. **Bitácora de Rondines**

Catálogos

1. **Definición de Exámenes**
2. **Definición de Permisos**
3. **Perfiles**
4. **Configuración de Perfiles**
5. **Visita Autorizada**
6. **Pase de Entrada**
7. **Lockers**
8. **Configuración de Gafetes y Lockers**
9. **Gafetes**
10. **Lista de Incidentes**
11. **Lista de Fallas**
12. **Configuración de Recorridos**
13. **Configuración de Recorridos Áreas de Inspección**

.. hint:: Para facilitar la comprensión y el uso del módulo, esta documentación se organiza de manera lógica siguiendo el flujo de procesos y no estrictamente separada entre formas y catálogos. Esto le permitirá comprender cómo cada componente interactúa y se integra con los demás dentro del contexto del control de accesos. A medida que avance en la documentación, encontrará más detalles sobre cada forma y catálogo, proporcionando ejemplos y guías paso a paso para su correcta implementación y utilización.

Definición de Permisos
======================

El **Catálogo de Definición de Permisos** es esencial para establecer y gestionar los permisos necesarios que se asignan a los perfiles de visitantes o empleados. Este catálogo se sincroniza con el **Catálogo de Definición de Exámenes** para garantizar que todos los requisitos necesarios sean cumplidos antes de otorgar un permiso.

Campos del Catálogo de Definición de Permisos
---------------------------------------------

1. **Nombre del Permiso o Certificación**: El nombre descriptivo del permiso o certificación.
2. **Requerimientos**: Los requisitos necesarios para obtener el permiso, que pueden incluir aprobaciones de exámenes u otros criterios específicos.
3. **Vigencia**: El período de validez del permiso o certificación.
4. **Vigencia Expresada en**:
    - **Ejemplo de documento del permiso/certificación**: Un documento que demuestre el permiso o certificación.
    - **Ejemplo en imagen**: Una imagen del documento que acredite el permiso o certificación.
5. **Examen**: El examen que debe ser aprobado para obtener el permiso, sincronizado con el **Catálogo de Definición de Exámenes**.
6. **Estado del Permiso/Certificación**: El estado actual del permiso o certificación.

Definición de Exámenes
----------------------

El **Catálogo de Definición de Exámenes** define los exámenes necesarios para ciertos permisos y perfiles. Este catálogo es utilizado por la **Forma de Definición de Permisos** para validar los requisitos.

Campos del Catálogo de Definición de Exámenes

1. **ID Forma**: Identificador único del examen.
2. **Nombre del Examen**: El nombre descriptivo del examen.

La sincronización entre el **Catálogo de Definición de Permisos** y el **Catálogo de Definición de Exámenes** garantiza que los permisos otorgados se basen en la aprobación de exámenes específicos. Esto asegura que solo las personas que cumplan con todos los requisitos necesarios puedan acceder a áreas restringidas o desempeñar ciertas funciones.

Ejemplo

1. **Catálogo de Definición de Exámenes**:
   - ID Forma: 001
   - Nombre del Examen: Examen de Seguridad en Alturas

2. **Catálogo de Definición de Permisos**:
   - Nombre del Permiso o Certificación: Acceso a Zonas Elevadas
   - Requerimientos: Aprobación del Examen de Seguridad en Alturas
   - Vigencia: 1 año
   - Vigencia Expresada en:
       - Documento del permiso/certificación
       - Imagen del documento
   - Examen: Examen de Seguridad en Alturas (ID Forma: 001)
   - Estado del Permiso/Certificación: Activo

En este ejemplo, el **Catálogo de Definición de Permisos** utiliza la información del **Catálogo de Definición de Exámenes** para validar que el permiso de **Acceso a Zonas Elevadas** solo sea otorgado a personas que hayan aprobado el **Examen de Seguridad en Alturas**.

Catálogos de Configuración y Definición
=======================================

En el módulo de **Accesos**, los catálogos de configuración y definición permite establecer y gestionar los parámetros y criterios que rigen el control de acceso en una ubicación. 
Estos catálogos permiten definir permisos, perfiles, exámenes y configuraciones necesarias para asegurar un entorno controlado y seguro. A continuación, se describen los catálogos más importantes de esta sección.

Definición de Exámenes
----------------------

Este catálogo permite definir los exámenes necesarios para ciertos perfiles de visitantes o empleados. Estos exámenes pueden ser requeridos para otorgar acceso a áreas específicas o para cumplir con requisitos de seguridad.

- **Nombre del Examen**: Nombre descriptivo del examen (e.g., Examen de Primeros Auxilios).
- **Descripción**: Descripción detallada del examen y su propósito.
- **Frecuencia**: Indica la frecuencia con la que el examen debe ser tomado (e.g., Anual, Semestral).
- **Responsable**: Persona o departamento encargado de administrar el examen.

Definición de Permisos
----------------------

Este catálogo permite definir los diferentes permisos que pueden ser asignados a perfiles de visitantes o empleados. Los permisos determinan las áreas y recursos a los que una persona puede acceder.

- **Nombre del Permiso**: Nombre descriptivo del permiso (e.g., Acceso a Áreas Restringidas).
- **Descripción**: Descripción detallada del permiso y las condiciones para su otorgamiento.
- **Duración**: Período de validez del permiso (e.g., Temporal, Permanente).
- **Requisitos**: Exámenes o condiciones que deben cumplirse para obtener el permiso.

Perfiles
--------

Este catálogo define los diferentes perfiles de visitantes y empleados que pueden tener acceso a la instalación. Cada perfil tiene un conjunto de permisos y requisitos específicos.

- **Nombre del Perfil**: Nombre descriptivo del perfil (e.g., Trabajador de Alturas, Visitante General).
- **Descripción**: Descripción detallada del perfil y su propósito dentro de la instalación.
- **Permisos Asociados**: Lista de permisos que se asignan a este perfil.
- **Requisitos de Exámenes**: Lista de exámenes que deben ser aprobados para obtener el perfil.

Configuración de Perfiles
-------------------------

Este catálogo permite configurar los detalles específicos de cada perfil, incluyendo los permisos y exámenes asociados. Es crucial para garantizar que los perfiles cumplan con todas las condiciones necesarias para el acceso seguro.

- **Perfil**: Selección del perfil a configurar.
- **Permisos Asociados**: Detalle de los permisos que se asignan al perfil.
- **Exámenes Requeridos**: Detalle de los exámenes que deben ser aprobados para obtener el perfil.
- **Observaciones**: Notas adicionales sobre la configuración del perfil.

Ejemplo de Configuración de Perfil: Trabajador de Alturas

1. **Definición de Exámenes**:
   - Nombre del Examen: Examen de Seguridad en Alturas
   - Descripción: Evaluación de habilidades y conocimientos necesarios para trabajar en alturas.
   - Frecuencia: Anual
   - Responsable: Departamento de Seguridad

2. **Definición de Permisos**:
   - Nombre del Permiso: Acceso a Zonas Elevadas
   - Descripción: Permite el acceso a áreas elevadas dentro de la instalación.
   - Duración: Permanente
   - Requisitos: Examen de Seguridad en Alturas aprobado

3. **Perfiles**:
   - Nombre del Perfil: Trabajador de Alturas
   - Descripción: Empleado autorizado para realizar trabajos en áreas elevadas.
   - Permisos Asociados: Acceso a Zonas Elevadas
   - Requisitos de Exámenes: Examen de Seguridad en Alturas

4. **Configuración de Perfiles**:
   - Perfil: Trabajador de Alturas
   - Permisos Asociados: Acceso a Zonas Elevadas
   - Exámenes Requeridos: Examen de Seguridad en Alturas
   - Observaciones: Este perfil debe renovarse anualmente tras la aprobación del examen.

Estos catálogos de configuración y definición son esenciales para establecer un sistema de control de accesos robusto y eficiente. Al definir y configurar adecuadamente los exámenes, permisos y perfiles, se asegura que solo personas debidamente autorizadas y preparadas puedan acceder a áreas críticas dentro de la instalación.