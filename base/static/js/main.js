define(['waitForImages'], function(){
	var interfaz = {
		config: {
			fadeInDelay: 750,
			fadeOutDelay: 750
		},
		elementos: {
			loader: $('#loader'),
			contenido: $('#base-contenido')
		},
		inicializar: function(){
			var url = '/static/img/background/menu.png';
			$('<img>').attr('src', url).load(function(){
				this.remove();
				$('body').css({'background-image':'url(' + url + ')'});
				$('body').waitForImages(function(){
					interfaz.mostrarInterfaz();
				});
			});
		},
		mostrarInterfaz: function(){
			this.elementos.loader.fadeOut(this.config.fadeOutDelay);
			this.elementos.contenido.fadeIn(this.config.fadeInDelay);
		}
	};

	$('.url').click(function(){
		location.href = $(this).data('url');
	});

	interfaz.inicializar();
});