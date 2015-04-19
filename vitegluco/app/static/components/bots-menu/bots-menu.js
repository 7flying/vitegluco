define(['knockout', 'text!./bots-menu.html'], function(ko, template) {

    function BotsMenuViewModel(params) {
	var self = this;
	this.alarmCount = ko.observable(10);
	this.captchaCount = ko.observable(2);
    }
    return { viewModel: BotsMenuViewModel, template: template };
});
