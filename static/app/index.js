(function($){
    $.fn.extend({
        donetyping: function(callback,timeout){
            timeout = timeout || 500;
            var timeoutReference,
                doneTyping = function(el){
                    if (!timeoutReference) return;
                    timeoutReference = null;
                    callback.call(el);
                };
            return this.each(function(i,el){
                var $el = $(el);
                $el.is(':input') && $el.on('keyup keypress',function(e){
                    if (e.type=='keyup' && e.keyCode!=8) return;
                    if (timeoutReference) clearTimeout(timeoutReference);
                    timeoutReference = setTimeout(function(){
                        doneTyping(el);
                    }, timeout);
                }).on('blur',function(){
                    doneTyping(el);
                });
            });
        }
    });
})(jQuery);

formValidation = {
    init: function(){
        this.$form = $('.registration-form');
        this.$firstName = this.$form.find('input[name="firstName"]');
       
        this.$email = this.$form.find('input[name="email"]');
                this.$dob = this.$form.find('input[name="dob"]');
                this.$location = this.$form.find('input[name="location"]');
                this.$startd = this.$form.find('input[name="startd"]');
                this.$pos = this.$form.find('input[name="pos"]'); 

                this.$res = this.$form.find('input[name="res"]');             
        this.$password = this.$form.find('input[name="password"]');
        this.$passwordToggle = this.$form.find('button.toggle-visibility');
        this.$submitButton = this.$form.find('button.submit');
       
        this.validatedFields = {
            firstName: false,
           
            email: false,
                        dob: false,
                        explain: false,
            res: false,
                        pos: false,
            password: false,
                        startd: false,
                        location: false

        };
       
        this.bindEvents();
    },
    bindEvents: function(){
        this.$firstName.donetyping(this.validateFirstNameHandler.bind(this));
                this.$email.donetyping(this.validateEmailHandler.bind(this));
        this.$dob.donetyping(this.validatedobHandler.bind(this));
                this.$pos.donetyping(this.validateposHandler.bind(this));
                
                this.$res.donetyping(this.validateresHandler.bind(this));
                this.$location.donetyping(this.validateEmailHandler.bind(this));
                this.$startd.donetyping(this.validateStartHandler.bind(this));
        this.$password.donetyping(this.validatePasswordHandler.bind(this));
        this.$passwordToggle.mousedown(this.togglePasswordVisibilityHandler.bind(this));
        this.$passwordToggle.click(function(e){e.preventDefault()});
        this.submitFormHandler.bind(this);
    },
    validateFirstNameHandler: function(){
        this.validatedFields.firstName = this.validateText(this.$firstName);
    },
        validateEmailHandler: function(){
        this.validatedFields.email = this.validateText(this.$email) && this.validateEmail(this.$email);
    },
    validatedobHandler: function(){
        this.validatedFields.dob = this.validateText(this.$dob);
    },

        
    validateresHandler: function(){
        this.validatedFields.res = this.validateText(this.$res);
    },
        validateposHandler: function(){
        this.validatedFields.dob = this.validateText(this.$pos);
    },
        validateLocationHandler: function(){
        this.validatedFields.dob = this.validateText(this.$location);
    },
   
        validateStartHandler: function(){
        this.validatedFields.startd = this.validateText(this.$startd);
    },
    validatePasswordHandler: function(){
        this.validatedFields.password = this.validateText(this.$password) && this.validatePassword(this.$password);
    },
    togglePasswordVisibilityHandler: function(){
        var html = '<input type="text" value="'+this.$password.val()+'">';
        var $passwordParent = this.$password.parent()
        var saved$password = this.$password.detach();
        $passwordParent.append(html);
        this.$passwordToggle.find('span').removeClass('glyphicon-eye-close').addClass('glyphicon-eye-open');
        this.$passwordToggle.one('mouseup mouseleave', (function(){
            $passwordParent.find('input').remove();
            $passwordParent.append(saved$password);
            this.$passwordToggle.find('span').removeClass('glyphicon-eye-open').addClass('glyphicon-eye-close');
        }).bind(this));
    },
    submitFormHandler: function(e){
        e.preventDefault();
        this.validateFirstNameHandler();
                this.validateEmailHandler();
        this.validatedobHandler();
       
               
        this.validateresHandler();
                this.validateposHandler();
                this.validateStartHandler();
                this.validateLocationHandler();
        this.validatePasswordHandler();
             
        if(this.validatedFields.firstName && this.validatedFields.email && this.validatedFields.dob && this.validatedFields.pos  && this.validatedFields.res && this.validatedFields.startd && this.validatedFields.location){
		this.$form.submit();
            this.$submitButton.addClass('loading').html('<span class="loading-spinner"></span>')
            setTimeout((function(){
      		this.$submitButton.submit()

            }).bind(this), 1500);
        }else{
            this.$submitButton.text('Please Fix the Errors');
            setTimeout((function(){
                if(this.$submitButton.text() == 'Please Fix the Errors'){
                    this.$submitButton.text('Sign Me Up');
                }
            }).bind(this), 3000)
        }
    },
   
    validateText: function($input){
        $input.parent().removeClass('invalid');
        $input.parent().find('span.label-text small.error').remove();
        if($input.val() != ''){
            return true;
        }else{
            $input.parent().addClass('invalid');
            $input.parent().find('span.label-text').append(' <small class="error">(Field is empty)</small>');
            return false;
        }
    },
    validateEmail: function($input){
        var regEx = /\S+@\S+\.\S+/;
        $input.parent().removeClass('invalid');
        $input.parent().find('span.label-text small.error').remove();
    if(regEx.test($input.val())){
            return true;
        }else{
            $input.parent().addClass('invalid');
            $input.parent().find('span.label-text').append(' <small class="error">(Email is invalid)</small>');
            return false;
        }
    },
    validatePassword: function($input){
            $input.parent().removeClass('invalid');
        $input.parent().find('span.label-text small.error').remove();
        if($input.val().length >= 8){
            return true;
        }else{
            $input.parent().addClass('invalid');
            $input.parent().find('span.label-text').append(' <small class="error">(Your password must longer than 7 characters)</small>');
            return false;
        }
    }
}.init();
