function expand_menu(expanding_group) {
    console.log('exp group:', expanding_group)
    let menulist = document.getElementById(expanding_group);
    if (menulist.classList.contains('expanded')) {
        menulist.classList.remove('expanded');
    } else {
        menulist.classList.add('expanded');
    }
}


//let edit_btns = document.querySelectorAll(".btn-edit");
//edit_btns.forEach(function(edit_btn) {
//    edit_btn.addEventListener("click", function(ev) {
//        ev.stopPropagation();
//
//    });
//});
//
//function toggleEditable(memberID) {
//    let field_set = document.getElementById(memberID);
//    if (field_set.disabled === true) {
//        field_set.disabled = false;
//    } else {
//        field_set.disabled = true;
//    }
//}
