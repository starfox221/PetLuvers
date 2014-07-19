$(document).ready(function () {
    var owner_input = $("#id_is_owner");
    var sitter_input = $("#id_is_sitter");

    var is_owner_change = function () {
        owner_input.is(":checked") ? $(".owner_info").show() : $(".owner_info").hide();
    };
    var is_sitter_change = function () {
        sitter_input.is(":checked") ? $(".sitter_info").show() : $(".sitter_info").hide();
    };

    owner_input.on("change", is_owner_change);
    sitter_input.on("change", is_sitter_change);

    is_owner_change();
    is_sitter_change();
})
