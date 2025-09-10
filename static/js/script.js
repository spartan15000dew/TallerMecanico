// Simulacion de base de datos de usuarios
        const usuariosValidos = [
            { nombreUsuario: 'admin', contrasena: 'admin123' },
            { nombreUsuario: 'usuario', contrasena: 'password123' },
            { nombreUsuario: 'demo', contrasena: 'demo2024' }
        ];

        // Elementos
        const formularioLogin = document.getElementById('loginForm');
        const entradaNombreUsuario = document.getElementById('username');
        const entradaContrasena = document.getElementById('password');
        const casillaRecordarDispositivo = document.getElementById('rememberDevice');
        const botonLogin = document.getElementById('loginButton');
        const mensajeExito = document.getElementById('successMessage');

        
        function mostrarError(elementoEntrada, elementoError, mensaje) {
            elementoEntrada.classList.add('error');
            elementoError.textContent = mensaje;
            elementoError.style.display = 'block';
        }

        // Función para mostrar el mensaje de exito
        function mostrarExito(mensaje) {
            mensajeExito.textContent = mensaje;
            mensajeExito.style.display = 'block';
            setTimeout(() => {
                mensajeExito.style.display = 'none';
            },10000);
        }

        // Función validación
        function validarFormulario() {
            let esValido = true;
            const nombreUsuario = entradaNombreUsuario.value.trim();
            const contrasena = entradaContrasena.value.trim();
            const errorNombreUsuario = document.getElementById('usernameError');
            const errorContrasena = document.getElementById('passwordError');

            // Validar nombre de usuario
            if (!nombreUsuario) {
                mostrarError(entradaNombreUsuario, errorNombreUsuario, 'El nombre de usuario es obligatorio');
                esValido = false;
            } else if (nombreUsuario.length < 3) {
                mostrarError(entradaNombreUsuario, errorNombreUsuario, 'El nombre de usuario debe tener al menos 3 caracteres');
                esValido = false;
            } else if (!/^[a-zA-Z0-9_]+$/.test(nombreUsuario)) {
                mostrarError(entradaNombreUsuario, errorNombreUsuario, 'El nombre de usuario solo puede contener letras, números y guiones bajos');
                esValido = false;
            }

            // Validar contraseña
            if (!contrasena) {
                mostrarError(entradaContrasena, errorContrasena, 'La contraseña es obligatoria');
                esValido = false;
            } else if (contrasena.length < 6) {
                mostrarError(entradaContrasena, errorContrasena, 'La contraseña debe tener al menos 6 caracteres');
                esValido = false;
            }

            return esValido;
        }

        // Para verificar credenciales
        function autenticarUsuario(nombreUsuario, contrasena) {
            return usuariosValidos.find(usuario => 
                usuario.nombreUsuario === nombreUsuario && usuario.contrasena === contrasena
            );
        }

        // Manejo del formulario
        formularioLogin.addEventListener('submit', function(e) {
            e.preventDefault();
            
            if (!validarFormulario()) {
                return;
            }

            const nombreUsuario = entradaNombreUsuario.value.trim();
            const contrasena = entradaContrasena.value.trim();

            // Deshabilitar botón durante la validacion
            botonLogin.disabled = true;
            botonLogin.textContent = 'Verificando...';

            // Simular un delay de autenticacion
            setTimeout(() => {
                const usuario = autenticarUsuario(nombreUsuario, contrasena);
                
                if (usuario) {
                    // Login exitoso
                    
                    mostrarExito(`¡Bienvenido, ${nombreUsuario}! Has iniciado sesión correctamente.`);
                    
                } else {
                    // Login fallido
                    const errorNombreUsuario = document.getElementById('usernameError');
                    const errorContrasena = document.getElementById('passwordError');
                    mostrarError(entradaNombreUsuario, errorNombreUsuario, 'Credenciales incorrectas');
                    mostrarError(entradaContrasena, errorContrasena, 'Credenciales incorrectas');
                }
                
                // Rehabilitar botón
                botonLogin.disabled = false;
                botonLogin.textContent = 'Iniciar Sesión';
            }, 1000);
        });

        // Agregar ayuda para desarrolladores
        console.log('Usuarios de prueba disponibles:');
        console.log('admin / admin123');
        console.log('usuario / password123');
        console.log('demo / demo2024');