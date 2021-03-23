const myOptions = [{
    name:'jQuery',
    value:'jquery'
    },{
    name:'Script',
    value:'script'
    },{
    name:'Disabled',
    value:'disabled',
    disabled:true
    },{
    name:'Net',
    value:'net'
    },{
    name:'CSS',
    value:'css'
    },{
    name:'Com',
    value:'com'
    }
]

$('#select_test').select({
data: myOptions
});
    
$('#example').select({
data: myOptions,
activeClass:'item-active',
disabledClass:'select-disabled',
itemDisabledClass:'item-disabled',
openClass:'select-open'
});

$('#example').select({
data: myOptions,
index: 1
});

$('#example').select({
    data: myOptions,
    index: 2
});
    


// disable/enable the dropdown
$('#example').select('disabled', boolean);
// get the selected option
$('#example').select('getName');
// get the selected option value
$('#example').select('getValue');
// select an option
$('#example').select('setSelect', index);
// up<a href="https://www.jqueryscript.net/time-clock/">date</a> the data
$('#example').select('update', data);

        