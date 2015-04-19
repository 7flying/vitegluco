define(['knockout', 'text!./generator.html'], function(ko, template) {
    Array.prototype.contains = function(element) {
	for (var i in this)
	    if (this[i] == element)
		return true;
	return false;
    };
    // key listener
    ko.bindingHandlers.executeOnEnter = {
	init: function(element, valueAccessor, allBindingsAccesor, viewModel) {
	    var allBindings = allBindingsAccesor();
	    $(element).keypress(function(event) {
		var keyCode = (event.which ? event.which : event.keyCode);
		if (keyCode === 13) {
		    allBindings.executeOnEnter.call(viewModel);
		    return false;
		}
		return true;
	    });
	}
    };
    
    function BotGeneratorViewModel(params) {
	var self = this;
	this.selectedOption = ko.observable("Twitter");
	this.enableTwitter = ko.observable(true);
	// Forms
	this.name = ko.observable();
	this.lastname = ko.observable();
	this.email = ko.observable();
	// Twitter specific
	this.username = ko.observable();

	// users
	this.tags = ko.observableArray([]);
	this.tag = ko.observable();
	
	this.onTwitter = function() {
	    self.enableTwitter(true);
	};
	this.onFace = function() {
	    self.enableTwitter(null);
	};
	this.submit = function() {
	};

	this.addTag = function() {
	    // If the tag is repeated ignore it.
	    if (!self.tags().contains(self.tag())) {
		self.tags.push(self.tag());
		// clear input
		$('#tagAdder').val('');
	    }
	};
	this.removeTag = function(tag) {
	    self.tags.remove(tag);
	};
    }
    return { viewModel: BotGeneratorViewModel, template: template };
});
