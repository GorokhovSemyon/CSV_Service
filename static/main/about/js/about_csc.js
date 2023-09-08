let my_table1 = document.querySelector('.strizka');
let my_table2 = document.querySelector('.boroda');
let my_table3 = document.querySelector('.uhod');
let my_table4 = document.querySelector('.britie');

const  a_str = document.querySelector('.striz');
const  a_bor = document.querySelector('.borod');
const  a_uh = document.querySelector('.uxod');
const  a_brit = document.querySelector('.brit');

a_str.addEventListener('click', function() {
	
	my_table1.classList.add("act");
	my_table1.classList.remove("no-act");
	my_table2.classList.add("no-act");
	my_table2.classList.remove("act");
	my_table3.classList.add("no-act");
	my_table3.classList.remove("act");
	my_table4.classList.add("no-act");
	my_table4.classList.remove("act");
})

a_bor.addEventListener('click', function() {
	//производим какие-то действия
	my_table1.classList.add("no-act");
	my_table1.classList.remove("act");
	my_table2.classList.add("act");
	my_table2.classList.remove("no-act");
	my_table3.classList.add("no-act");
	my_table3.classList.remove("act");
	my_table4.classList.add("no-act");
	my_table4.classList.remove("act");
})

a_uh.addEventListener('click', function() {
	//производим какие-то действия
	my_table1.classList.add("no-act");
	my_table1.classList.remove("act");
	my_table2.classList.add("no-act");
	my_table2.classList.remove("act");
	my_table3.classList.add("act");
	my_table3.classList.remove("no-act");
	my_table4.classList.add("no-act");
	my_table4.classList.remove("act");
})

a_brit.addEventListener('click', function() {
	//производим какие-то действия
	my_table1.classList.add("no-act");
	my_table1.classList.remove("act");
	my_table2.classList.add("no-act");
	my_table2.classList.remove("act");
	my_table3.classList.add("no-act");
	my_table3.classList.remove("act");
	my_table4.classList.add("act");
	my_table4.classList.remove("no-act");
})