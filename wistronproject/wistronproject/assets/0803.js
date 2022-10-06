// 切換頁面
var DiversityDiv;
var LaborDiv;
var LaborButton;
var DiversityButton;

// 多元共融時間軸按鈕
var DiversityChangeNowendButton;
var DiversityNowendPic;
var DiversityChangeMonthyearButton;
var DiversityMonthyearPic;
var DiversitythreemonthButton;
var DiversitysixmonthButton;
var DiversitytenmonthButton;

// 多元共融DIV
var Diversitynowyear;
var Diversitynowmonth;
var Diversitythreey;
var Diversityfivey
var Diversityteny;
var Diversitythreem;
var Diversitysixm;
var Diversitytenm;

// 勞工關係時間軸按鈕
var LaborChangeNowendButton;
var LaborNowendPic;
var LaborChangeMonthyearButton;
var LaborMonthyearPic;
var LaborthreemonthButton;
var LaborsixmonthButton;
var LabortenmonthButton;

// 勞工關係DIV
var Labornowyear;
var Labornowmonth;
var Laborthreey;
var Laborfivey
var Laborteny;
var Laborthreem;
var Laborsixm;
var Labortenm;

var Mainbutton;
var MainDiv;

const myInterval = setInterval(() => {
    let error = false;
    // 切換頁面
    DiversityDiv = document.getElementById('DiversityInclusion');
    LaborDiv = document.getElementById('LaborRelations');
    LaborButton = document.getElementById('Labor');
    DiversityButton = document.getElementById('Diversity');

    // 多元共融時間軸按鈕
    DiversityChangeNowendButton = document.getElementById('DiversityChangeNowend');
    DiversityNowendPic = document.getElementById('DiversityNowend');
    DiversityChangeMonthyearButton = document.getElementById('DiversityChangeMonthyear');
    DiversityMonthyearPic = document.getElementById('DiversityMonthyear');
    DiversitythreemonthButton = document.getElementById('Diversitythreemonth');
    DiversitysixmonthButton = document.getElementById('Diversitysixmonth');
    DiversitytenmonthButton = document.getElementById('Diversitytenmonth');
    // 多元共融DIV
    Diversitynowyear = document.getElementById('Diversitynowyear');
    Diversitynowmonth = document.getElementById('Diversitynowmonth');
    Diversitythreey = document.getElementById('Diversitythreey');
    Diversityfivey = document.getElementById('Diversityfivey');
    Diversityteny = document.getElementById('Diversityteny');
    Diversitythreem = document.getElementById('Diversitythreem');
    Diversitysixm = document.getElementById('Diversitysixm');
    Diversitytenm = document.getElementById('Diversitytenm');

    // 勞工關係時間軸按鈕
    LaborChangeNowendButton = document.getElementById('LaborChangeNowend');
    LaborNowendPic = document.getElementById('LaborNowend');
    LaborChangeMonthyearButton = document.getElementById('LaborChangeMonthyear');
    LaborMonthyearPic = document.getElementById('LaborMonthyear');
    LaborthreemonthButton = document.getElementById('Laborthreemonth');
    LaborsixmonthButton = document.getElementById('Laborsixmonth');
    LabortenmonthButton = document.getElementById('Labortenmonth');
    // 勞工關係DIV
    Labornowyear = document.getElementById('Labornowyear');
    Labornowmonth = document.getElementById('Labornowmonth');
    Laborthreey = document.getElementById('Laborthreey');
    Laborfivey = document.getElementById('Laborfivey');
    Laborteny = document.getElementById('Laborteny');
    Laborthreem = document.getElementById('Laborthreem');
    Laborsixm = document.getElementById('Laborsixm');
    Labortenm = document.getElementById('Labortenm');

    Mainbutton = document.getElementById('mainbutton');
    MainDiv = document.getElementById('main');

    LaborDiv.style.display = 'none';
    DiversityDiv.style.display = 'none';
    Mainbutton.style.backgroundColor = '#3B8E7E'
    Mainbutton.style.color = '#fff'

    // 切換頁面
    if (DiversityDiv == null) {
        error = true;
    }
    if (LaborDiv == null) {
        error = true;
    }
    if (LaborButton == null) {
        error = true;
    }
    if (DiversityButton == null) {
        error = true;
    }

    // 多元共融時間軸按鈕
    if (DiversityChangeNowendButton == null) {
        error = true;
    }
    if (DiversityNowendPic == null) {
        error = true;
    }
    if (DiversityChangeMonthyearButton == null) {
        error = true;
    }
    if (DiversityMonthyearPic == null) {
        error = true;
    }
    if (DiversitythreemonthButton == null) {
        error = true;
    }
    if (DiversitysixmonthButton == null) {
        error = true;
    }
    if (DiversitytenmonthButton == null) {
        error = true;
    }

    // 多元共融DIV
    if (Diversitynowyear == null) {
        error = true;
    }
    if (Diversitynowmonth == null) {
        error = true;
    }
    if (Diversitythreey == null) {
        error = true;
    }
    if (Diversityfivey == null) {
        error = true;
    }
    if (Diversityteny == null) {
        error = true;
    }
    if (Diversitythreem == null) {
        error = true;
    }
    if (Diversitysixm == null) {
        error = true;
    }
    if (Diversitytenm == null) {
        error = true;
    }

    // 勞工關係時間軸按鈕
    if (LaborChangeNowendButton == null) {
        error = true;
    }
    if (LaborNowendPic == null) {
        error = true;
    }
    if (LaborChangeMonthyearButton == null) {
        error = true;
    }
    if (LaborMonthyearPic == null) {
        error = true;
    }
    if (LaborthreemonthButton == null) {
        error = true;
    }
    if (LaborsixmonthButton == null) {
        error = true;
    }
    if (LabortenmonthButton == null) {
        error = true;
    }
    // 勞工關係DIV
    if (Labornowyear == null) {
        error = true;
    }
    if (Labornowmonth == null) {
        error = true;
    }
    if (Laborthreey == null) {
        error = true;
    }
    if (Laborfivey == null) {
        error = true;
    }
    if (Laborteny == null) {
        error = true;
    }
    if (Laborthreem == null) {
        error = true;
    }
    if (Laborsixm == null) {
        error = true;
    }
    if (Labortenm == null) {
        error = true;
    }

    if (Mainbutton == null) {
        error = true;
    }
    if (MainDiv == null) {
        error = true;
    }

    if (!error) {
        AddEventListener();
    }
}, 200);
function AddEventListener() {
    clearInterval(myInterval);
    LaborButton.addEventListener('click', Laborfunction)
    DiversityButton.addEventListener('click', Diversityfunction)

    DiversityChangeNowendButton.addEventListener('click', DiversityChangeNowendfunction)
    DiversityChangeMonthyearButton.addEventListener('click', DiversityChangeMonthyearfunction)
    DiversitythreemonthButton.addEventListener('click', DiversityThreeMonthButtonfunction)
    DiversitysixmonthButton.addEventListener('click', DiversitySixMonthButtonfunction)
    DiversitytenmonthButton.addEventListener('click', DiversityTenMonthButtonfunction)

    LaborChangeNowendButton.addEventListener('click', LaborChangeNowendfunction)
    LaborChangeMonthyearButton.addEventListener('click', LaborChangeMonthyearfunction)
    LaborthreemonthButton.addEventListener('click', LaborThreeMonthButtonfunction)
    LaborsixmonthButton.addEventListener('click', LaborSixMonthButtonfunction)
    LabortenmonthButton.addEventListener('click', LaborTenMonthButtonfunction)

    Mainbutton.addEventListener('click', Mainfunction)
}
// 人資永續切換頁面
function Mainfunction() {
    MainDiv.style.display = 'inline-block';
    DiversityDiv.style.display = 'none';
    LaborDiv.style.display = 'none';
    Mainbutton.style.backgroundColor = '#3B8E7E'
    Mainbutton.style.color = '#fff'
    DiversityButton.style.backgroundColor = '#fff'
    DiversityButton.style.color = '#111111'
    LaborButton.style.backgroundColor = '#fff'
    LaborButton.style.color = '#111111'
    Diversitynowmonth.style.display = 'none';
    Diversitynowyear.style.display = 'none';
    Diversitythreey.style.display = 'none';
    Diversityfivey.style.display = 'none';
    Diversityteny.style.display = 'none';
    Diversitythreem.style.display = 'none';
    Diversitysixm.style.display = 'none';
    Diversitytenm.style.display = 'none';
    DiversitythreemonthButton.style.display = 'none';
    DiversitysixmonthButton.style.display = 'none';
    DiversitytenmonthButton.style.display = 'none';
}

// 多元共融頁面
function Diversityfunction() {
    MainDiv.style.display = 'none';
    DiversityNowendPic.src = 'assets/多元共融現況.png'
    Mainbutton.style.backgroundColor = '#fff'
    Mainbutton.style.color = '#111111'
    DiversityDiv.style.display = 'inline-block';
    LaborDiv.style.display = 'none';
    DiversityButton.style.backgroundColor = '#E73A5F'
    DiversityButton.style.color = '#fff'
    LaborButton.style.backgroundColor = '#fff'
    LaborButton.style.color = '#111111'
    Diversitynowmonth.style.display = 'inline-block';
    Diversitynowyear.style.display = 'none';
    Diversitythreey.style.display = 'none';
    Diversityfivey.style.display = 'none';
    Diversityteny.style.display = 'none';
    Diversitythreem.style.display = 'none';
    Diversitysixm.style.display = 'none';
    Diversitytenm.style.display = 'none';
    DiversitythreemonthButton.style.display = 'none';
    DiversitysixmonthButton.style.display = 'none';
    DiversitytenmonthButton.style.display = 'none';
}
// 多元共融現況歷史切換
function DiversityChangeNowendfunction() {
    if (DiversityChangeNowendButton.innerHTML == '現況') {
        if (DiversityChangeMonthyearButton.innerHTML == '月') {
            DiversityNowendPic.src = 'assets/多元共融歷史.png';
            DiversityChangeNowendButton.innerHTML = '歷史';
            DiversitythreemonthButton.style.backgroundColor = '#E73A5F'
            DiversitythreemonthButton.style.color = '#fff'
            DiversitysixmonthButton.style.backgroundColor = '#fff'
            DiversitysixmonthButton.style.color = '#11111'
            DiversitytenmonthButton.style.backgroundColor = '#fff'
            DiversitytenmonthButton.style.color = '#11111'
            DiversitythreemonthButton.style.display = 'inline-block';
            DiversitythreemonthButton.innerHTML = '近三月';
            DiversitysixmonthButton.style.display = 'inline-block';
            DiversitysixmonthButton.innerHTML = '近六月';
            DiversitytenmonthButton.style.display = 'inline-block';
            DiversitytenmonthButton.innerHTML = '近十月';
            Diversitynowmonth.style.display = 'none'
            Diversitynowyear.style.display = 'none';
            Diversitythreey.style.display = 'none';
            Diversityfivey.style.display = 'none';
            Diversityteny.style.display = 'none';
            Diversitythreem.style.display = 'inline-block';
            Diversitysixm.style.display = 'none';
            Diversitytenm.style.display = 'none';
        } else if (DiversityChangeMonthyearButton.innerHTML == '年') {
            DiversityNowendPic.src = 'assets/多元共融歷史.png';
            DiversityChangeNowendButton.innerHTML = '歷史';
            DiversitythreemonthButton.style.backgroundColor = '#E73A5F'
            DiversitythreemonthButton.style.color = '#fff'
            DiversitysixmonthButton.style.backgroundColor = '#fff'
            DiversitysixmonthButton.style.color = '#11111'
            DiversitytenmonthButton.style.backgroundColor = '#fff'
            DiversitytenmonthButton.style.color = '#11111'
            DiversitythreemonthButton.style.display = 'inline-block';
            DiversitythreemonthButton.innerHTML = '近三年';
            DiversitysixmonthButton.style.display = 'inline-block';
            DiversitysixmonthButton.innerHTML = '近五年';
            DiversitytenmonthButton.style.display = 'inline-block';
            DiversitytenmonthButton.innerHTML = '近十年';
            Diversitynowmonth.style.display = 'none'
            Diversitynowyear.style.display = 'none';
            Diversitythreey.style.display = 'inline-block';
            Diversityfivey.style.display = 'none';
            Diversityteny.style.display = 'none';
            Diversitythreem.style.display = 'none';
            Diversitysixm.style.display = 'none';
            Diversitytenm.style.display = 'none';
        }
    }
    else if (DiversityChangeNowendButton.innerHTML == '歷史') {
        if (DiversityChangeMonthyearButton.innerHTML == '月') {
            DiversityNowendPic.src = 'assets/多元共融現況.png'
            DiversityChangeNowendButton.innerHTML = '現況';
            DiversitythreemonthButton.style.backgroundColor = '#E73A5F'
            DiversitythreemonthButton.style.color = '#fff'
            DiversitysixmonthButton.style.backgroundColor = '#fff'
            DiversitysixmonthButton.style.color = '#111111'
            DiversitytenmonthButton.style.backgroundColor = '#fff'
            DiversitytenmonthButton.style.color = '#111111'
            DiversitythreemonthButton.style.display = 'none';
            DiversitysixmonthButton.style.display = 'none';
            DiversitytenmonthButton.style.display = 'none';
            Diversitynowmonth.style.display = 'inline-block'
            Diversitynowyear.style.display = 'none';
            Diversitythreey.style.display = 'none';
            Diversityfivey.style.display = 'none';
            Diversityteny.style.display = 'none';
            Diversitythreem.style.display = 'none';
            Diversitysixm.style.display = 'none';
            Diversitytenm.style.display = 'none';

        } else if (DiversityChangeMonthyearButton.innerHTML == '年') {
            DiversityNowendPic.src = 'assets/多元共融現況.png'
            DiversityChangeNowendButton.innerHTML = '現況';
            DiversitythreemonthButton.style.backgroundColor = '#E73A5F'
            DiversitythreemonthButton.style.color = '#fff'
            DiversitysixmonthButton.style.backgroundColor = '#fff'
            DiversitysixmonthButton.style.color = '#111111'
            DiversitytenmonthButton.style.backgroundColor = '#fff'
            DiversitytenmonthButton.style.color = '#111111'
            DiversitythreemonthButton.style.display = 'none';
            DiversitysixmonthButton.style.display = 'none';
            DiversitytenmonthButton.style.display = 'none';
            Diversitynowmonth.style.display = 'none'
            Diversitynowyear.style.display = 'inline-block'
            Diversitythreey.style.display = 'none'
            Diversityfivey.style.display = 'none';
            Diversityteny.style.display = 'none';
            Diversitythreem.style.display = 'none';
            Diversitysixm.style.display = 'none';
            Diversitytenm.style.display = 'none';

        }
    }
}
// 多元共融年月切換
function DiversityChangeMonthyearfunction() {
    if (DiversityChangeMonthyearButton.innerHTML == '月') {
        if (DiversityChangeNowendButton.innerHTML == '現況') {
            DiversityMonthyearPic.src = 'assets/多元共融年.png';
            DiversityChangeMonthyearButton.innerHTML = '年';
            DiversitythreemonthButton.style.backgroundColor = '#E73A5F'
            DiversitythreemonthButton.style.color = '#fff'
            DiversitysixmonthButton.style.backgroundColor = '#fff'
            DiversitysixmonthButton.style.color = '#111111'
            DiversitytenmonthButton.style.backgroundColor = '#fff'
            DiversitytenmonthButton.style.color = '#111111'
            DiversitythreemonthButton.innerHTML = '近三月';
            DiversitythreemonthButton.style.display = 'none';
            DiversitysixmonthButton.innerHTML = '近六月';
            DiversitysixmonthButton.style.display = 'none';
            DiversitytenmonthButton.innerHTML = '近十月';
            DiversitytenmonthButton.style.display = 'none';
            Diversitynowmonth.style.display = 'none'
            Diversitynowyear.style.display = 'inline-block';
            Diversitythreey.style.display = 'none';
            Diversityfivey.style.display = 'none';
            Diversityteny.style.display = 'none';
            Diversitythreem.style.display = 'none';
            Diversitysixm.style.display = 'none';
            Diversitytenm.style.display = 'none';
        } else if (DiversityChangeNowendButton.innerHTML == '歷史') {
            DiversityMonthyearPic.src = 'assets/多元共融年.png';
            DiversityChangeMonthyearButton.innerHTML = '年';
            DiversitythreemonthButton.style.backgroundColor = '#E73A5F'
            DiversitythreemonthButton.style.color = '#fff'
            DiversitysixmonthButton.style.backgroundColor = '#fff'
            DiversitysixmonthButton.style.color = '#111111'
            DiversitytenmonthButton.style.backgroundColor = '#fff'
            DiversitytenmonthButton.style.color = '#111111'
            DiversitythreemonthButton.style.display = 'inline-block';
            DiversitythreemonthButton.innerHTML = '近三年';
            DiversitysixmonthButton.style.display = 'inline-block';
            DiversitysixmonthButton.innerHTML = '近五年';
            DiversitytenmonthButton.style.display = 'inline-block';
            DiversitytenmonthButton.innerHTML = '近十年';
            Diversitynowmonth.style.display = 'none'
            Diversitynowyear.style.display = 'none';
            Diversitythreey.style.display = 'inline-block';
            Diversityfivey.style.display = 'none';
            Diversityteny.style.display = 'none';
            Diversitythreem.style.display = 'none';
            Diversitysixm.style.display = 'none';
            Diversitytenm.style.display = 'none';
        }
    }
    else if (DiversityChangeMonthyearButton.innerHTML == '年') {
        if (DiversityChangeNowendButton.innerHTML == '現況') {
            DiversityMonthyearPic.src = 'assets/多元共融月.png'
            DiversityChangeMonthyearButton.innerHTML = '月';
            DiversitythreemonthButton.style.backgroundColor = '#E73A5F'
            DiversitythreemonthButton.style.color = '#fff'
            DiversitysixmonthButton.style.backgroundColor = '#fff'
            DiversitysixmonthButton.style.color = '#111111'
            DiversitytenmonthButton.style.backgroundColor = '#fff'
            DiversitytenmonthButton.style.color = '#111111'
            DiversitythreemonthButton.innerHTML = '近三年';
            DiversitythreemonthButton.style.display = 'none';
            DiversitysixmonthButton.innerHTML = '近五年';
            DiversitysixmonthButton.style.display = 'none';
            DiversitytenmonthButton.innerHTML = '近十年';
            DiversitytenmonthButton.style.display = 'none';
            Diversitynowmonth.style.display = 'inline-block'
            Diversitynowyear.style.display = 'none';
            Diversitythreey.style.display = 'none';
            Diversityfivey.style.display = 'none';
            Diversityteny.style.display = 'none';
            Diversitythreem.style.display = 'none';
            Diversitysixm.style.display = 'none';
            Diversitytenm.style.display = 'none';
        } else if (DiversityChangeNowendButton.innerHTML == '歷史') {
            DiversityMonthyearPic.src = 'assets/多元共融月.png'
            DiversityChangeMonthyearButton.innerHTML = '月';
            DiversitythreemonthButton.style.backgroundColor = '#E73A5F'
            DiversitythreemonthButton.style.color = '#fff'
            DiversitysixmonthButton.style.backgroundColor = '#fff'
            DiversitysixmonthButton.style.color = '#111111'
            DiversitytenmonthButton.style.backgroundColor = '#fff'
            DiversitytenmonthButton.style.color = '#111111'
            DiversitythreemonthButton.style.display = 'inline-block';
            DiversitythreemonthButton.innerHTML = '近三月';
            DiversitysixmonthButton.style.display = 'inline-block';
            DiversitysixmonthButton.innerHTML = '近六月';
            DiversitytenmonthButton.style.display = 'inline-block';
            DiversitytenmonthButton.innerHTML = '近十月';
            Diversitynowmonth.style.display = 'none'
            Diversitynowyear.style.display = 'none';
            Diversitythreey.style.display = 'none';
            Diversityfivey.style.display = 'none';
            Diversityteny.style.display = 'none';
            Diversitythreem.style.display = 'inline-block';
            Diversitysixm.style.display = 'none';
            Diversitytenm.style.display = 'none';
        }
    }
}
// 多元共融三個月/年按鈕
function DiversityThreeMonthButtonfunction() {
    if (DiversityChangeNowendButton.innerHTML == '歷史' && DiversityChangeMonthyearButton.innerHTML == '月') {
        DiversitythreemonthButton.style.backgroundColor = '#E73A5F'
        DiversitythreemonthButton.style.color = '#fff'
        DiversitysixmonthButton.style.backgroundColor = '#fff'
        DiversitysixmonthButton.style.color = '#111111'
        DiversitytenmonthButton.style.backgroundColor = '#fff'
        DiversitytenmonthButton.style.color = '#111111'
        Diversitynowmonth.style.display = 'none'
        Diversitynowyear.style.display = 'none';
        Diversitythreey.style.display = 'none';
        Diversityfivey.style.display = 'none';
        Diversityteny.style.display = 'none';
        Diversitythreem.style.display = 'inline-block';
        Diversitysixm.style.display = 'none';
        Diversitytenm.style.display = 'none';
    } else if (DiversityChangeNowendButton.innerHTML == '歷史' && DiversityChangeMonthyearButton.innerHTML == '年') {
        DiversitythreemonthButton.style.backgroundColor = '#E73A5F'
        DiversitythreemonthButton.style.color = '#fff'
        DiversitysixmonthButton.style.backgroundColor = '#fff'
        DiversitysixmonthButton.style.color = '#111111'
        DiversitytenmonthButton.style.backgroundColor = '#fff'
        DiversitytenmonthButton.style.color = '#111111'
        Diversitynowmonth.style.display = 'none'
        Diversitynowyear.style.display = 'none';
        Diversitythreey.style.display = 'inline-block';
        Diversityfivey.style.display = 'none';
        Diversityteny.style.display = 'none';
        Diversitythreem.style.display = 'none';
        Diversitysixm.style.display = 'none';
        Diversitytenm.style.display = 'none';
    }
}
// 多元共融六個月/五年按鈕
function DiversitySixMonthButtonfunction() {
    if (DiversityChangeNowendButton.innerHTML == '歷史' && DiversityChangeMonthyearButton.innerHTML == '月') {
        DiversitythreemonthButton.style.backgroundColor = '#fff'
        DiversitythreemonthButton.style.color = '#111111'
        DiversitysixmonthButton.style.backgroundColor = '#E73A5F'
        DiversitysixmonthButton.style.color = '#fff'
        DiversitytenmonthButton.style.backgroundColor = '#fff'
        DiversitytenmonthButton.style.color = '#111111'
        Diversitynowmonth.style.display = 'none'
        Diversitynowyear.style.display = 'none';
        Diversitythreey.style.display = 'none';
        Diversityfivey.style.display = 'none';
        Diversityteny.style.display = 'none';
        Diversitythreem.style.display = 'none';
        Diversitysixm.style.display = 'inline-block';
        Diversitytenm.style.display = 'none';
    } else if (DiversityChangeNowendButton.innerHTML == '歷史' && DiversityChangeMonthyearButton.innerHTML == '年') {
        DiversitythreemonthButton.style.backgroundColor = '#fff'
        DiversitythreemonthButton.style.color = '#111111'
        DiversitysixmonthButton.style.backgroundColor = '#E73A5F'
        DiversitysixmonthButton.style.color = '#fff'
        DiversitytenmonthButton.style.backgroundColor = '#fff'
        DiversitytenmonthButton.style.color = '#111111'
        Diversitynowmonth.style.display = 'none'
        Diversitynowyear.style.display = 'none';
        Diversitythreey.style.display = 'none';
        Diversityfivey.style.display = 'inline-block';
        Diversityteny.style.display = 'none';
        Diversitythreem.style.display = 'none';
        Diversitysixm.style.display = 'none';
        Diversitytenm.style.display = 'none';
    }
}
// 多元共融十個月/年按鈕
function DiversityTenMonthButtonfunction() {
    if (DiversityChangeNowendButton.innerHTML == '歷史' && DiversityChangeMonthyearButton.innerHTML == '月') {
        DiversitythreemonthButton.style.backgroundColor = '#fff'
        DiversitythreemonthButton.style.color = '#111111'
        DiversitysixmonthButton.style.backgroundColor = '#fff'
        DiversitysixmonthButton.style.color = '#111111'
        DiversitytenmonthButton.style.backgroundColor = '#E73A5F'
        DiversitytenmonthButton.style.color = '#fff'
        Diversitynowmonth.style.display = 'none'
        Diversitynowyear.style.display = 'none';
        Diversitythreey.style.display = 'none';
        Diversityfivey.style.display = 'none';
        Diversityteny.style.display = 'none';
        Diversitythreem.style.display = 'none';
        Diversitysixm.style.display = 'none';
        Diversitytenm.style.display = 'inline-block';
    } else if (DiversityChangeNowendButton.innerHTML == '歷史' && DiversityChangeMonthyearButton.innerHTML == '年') {
        DiversitythreemonthButton.style.backgroundColor = '#fff'
        DiversitythreemonthButton.style.color = '#111111'
        DiversitysixmonthButton.style.backgroundColor = '#fff'
        DiversitysixmonthButton.style.color = '#111111'
        DiversitytenmonthButton.style.backgroundColor = '#E73A5F'
        DiversitytenmonthButton.style.color = '#fff'
        Diversitynowmonth.style.display = 'none'
        Diversitynowyear.style.display = 'none';
        Diversitythreey.style.display = 'none';
        Diversityfivey.style.display = 'none';
        Diversityteny.style.display = 'inline-block';
        Diversitythreem.style.display = 'none';
        Diversitysixm.style.display = 'none';
        Diversitytenm.style.display = 'none';
    }
}


// 勞工關係頁面
function Laborfunction() {
    MainDiv.style.display = 'none';
    LaborNowendPic.src = 'assets/勞工關係現況.png'
    Mainbutton.style.backgroundColor = '#fff'
    Mainbutton.style.color = '#111111'
    DiversityDiv.style.display = 'none';
    LaborDiv.style.display = 'inline-block';
    console.log('Button is clicked');
    LaborButton.style.backgroundColor = '#117B9E'
    DiversityButton.style.backgroundColor = '#fff'
    LaborButton.style.color = '#fff'
    DiversityButton.style.color = '#111111'
    Labornowmonth.style.display = 'inline-block';
    Labornowyear.style.display = 'none';
    Laborthreey.style.display = 'none';
    Laborfivey.style.display = 'none';
    Laborteny.style.display = 'none';
    Laborthreem.style.display = 'none';
    Laborsixm.style.display = 'none';
    Labortenm.style.display = 'none';
    LaborthreemonthButton.style.display = 'none';
    LaborsixmonthButton.style.display = 'none';
    LabortenmonthButton.style.display = 'none';
}
// 勞工關係現況歷史切換
function LaborChangeNowendfunction() {
    if (LaborChangeNowendButton.innerHTML == '現況') {
        if (LaborChangeMonthyearButton.innerHTML == '月') {
            LaborNowendPic.src = 'assets/勞工關係歷史.png';
            LaborChangeNowendButton.innerHTML = '歷史';
            LaborthreemonthButton.style.backgroundColor = '#117B9E'
            LaborthreemonthButton.style.color = '#fff'
            LaborsixmonthButton.style.backgroundColor = '#fff'
            LaborsixmonthButton.style.color = '#11111'
            LabortenmonthButton.style.backgroundColor = '#fff'
            LabortenmonthButton.style.color = '#11111'
            LaborthreemonthButton.style.display = 'inline-block';
            LaborthreemonthButton.innerHTML = '近三月';
            LaborsixmonthButton.style.display = 'inline-block';
            LaborsixmonthButton.innerHTML = '近六月';
            LabortenmonthButton.style.display = 'inline-block';
            LabortenmonthButton.innerHTML = '近十月';
            Labornowmonth.style.display = 'none'
            Labornowyear.style.display = 'none';
            Laborthreey.style.display = 'none';
            Laborfivey.style.display = 'none';
            Laborteny.style.display = 'none';
            Laborthreem.style.display = 'inline-block';
            Laborsixm.style.display = 'none';
            Labortenm.style.display = 'none';
        } else if (LaborChangeMonthyearButton.innerHTML == '年') {
            LaborNowendPic.src = 'assets/勞工關係歷史.png';
            LaborChangeNowendButton.innerHTML = '歷史';
            LaborthreemonthButton.style.backgroundColor = '#117B9E'
            LaborthreemonthButton.style.color = '#fff'
            LaborsixmonthButton.style.backgroundColor = '#fff'
            LaborsixmonthButton.style.color = '#11111'
            LabortenmonthButton.style.backgroundColor = '#fff'
            LabortenmonthButton.style.color = '#11111'
            LaborthreemonthButton.style.display = 'inline-block';
            LaborthreemonthButton.innerHTML = '近三年';
            LaborsixmonthButton.style.display = 'inline-block';
            LaborsixmonthButton.innerHTML = '近五年';
            LabortenmonthButton.style.display = 'inline-block';
            LabortenmonthButton.innerHTML = '近十年';
            Labornowmonth.style.display = 'none'
            Labornowyear.style.display = 'none';
            Laborthreey.style.display = 'inline-block';
            Laborfivey.style.display = 'none';
            Laborteny.style.display = 'none';
            Laborthreem.style.display = 'none';
            Laborsixm.style.display = 'none';
            Labortenm.style.display = 'none';
        }
    }
    else if (LaborChangeNowendButton.innerHTML == '歷史') {
        if (LaborChangeMonthyearButton.innerHTML == '月') {
            LaborNowendPic.src = 'assets/勞工關係現況.png'
            LaborChangeNowendButton.innerHTML = '現況';
            LaborthreemonthButton.style.backgroundColor = '#117B9E'
            LaborthreemonthButton.style.color = '#fff'
            LaborsixmonthButton.style.backgroundColor = '#fff'
            LaborsixmonthButton.style.color = '#111111'
            LabortenmonthButton.style.backgroundColor = '#fff'
            LabortenmonthButton.style.color = '#111111'
            LaborthreemonthButton.style.display = 'none';
            LaborsixmonthButton.style.display = 'none';
            LabortenmonthButton.style.display = 'none';
            Labornowmonth.style.display = 'inline-block'
            Labornowyear.style.display = 'none';
            Laborthreey.style.display = 'none';
            Laborfivey.style.display = 'none';
            Laborteny.style.display = 'none';
            Laborthreem.style.display = 'none';
            Laborsixm.style.display = 'none';
            Labortenm.style.display = 'none';

        } else if (LaborChangeMonthyearButton.innerHTML == '年') {
            LaborNowendPic.src = 'assets/勞工關係現況.png'
            LaborChangeNowendButton.innerHTML = '現況';
            LaborthreemonthButton.style.backgroundColor = '#117B9E'
            LaborthreemonthButton.style.color = '#fff'
            LaborsixmonthButton.style.backgroundColor = '#fff'
            LaborsixmonthButton.style.color = '#111111'
            LabortenmonthButton.style.backgroundColor = '#fff'
            LabortenmonthButton.style.color = '#111111'
            LaborthreemonthButton.style.display = 'none';
            LaborsixmonthButton.style.display = 'none';
            LabortenmonthButton.style.display = 'none';
            Labornowmonth.style.display = 'none'
            Labornowyear.style.display = 'inline-block'
            Laborthreey.style.display = 'none'
            Laborfivey.style.display = 'none';
            Laborteny.style.display = 'none';
            Laborthreem.style.display = 'none';
            Laborsixm.style.display = 'none';
            Labortenm.style.display = 'none';

        }
    }
}
// 勞工關係年月切換
function LaborChangeMonthyearfunction() {
    if (LaborChangeMonthyearButton.innerHTML == '月') {
        if (LaborChangeNowendButton.innerHTML == '現況') {
            LaborMonthyearPic.src = 'assets/勞工關係年.png';
            LaborChangeMonthyearButton.innerHTML = '年';
            LaborthreemonthButton.style.backgroundColor = '#117B9E'
            LaborthreemonthButton.style.color = '#fff'
            LaborsixmonthButton.style.backgroundColor = '#fff'
            LaborsixmonthButton.style.color = '#111111'
            LabortenmonthButton.style.backgroundColor = '#fff'
            LabortenmonthButton.style.color = '#111111'
            LaborthreemonthButton.style.display = 'none';
            LaborsixmonthButton.style.display = 'none';
            LabortenmonthButton.style.display = 'none';
            Labornowmonth.style.display = 'none'
            Labornowyear.style.display = 'inline-block';
            Laborthreey.style.display = 'none';
            Laborfivey.style.display = 'none';
            Laborteny.style.display = 'none';
            Laborthreem.style.display = 'none';
            Laborsixm.style.display = 'none';
            Labortenm.style.display = 'none';
        } else if (LaborChangeNowendButton.innerHTML == '歷史') {
            LaborMonthyearPic.src = 'assets/勞工關係年.png';
            LaborChangeMonthyearButton.innerHTML = '年';
            LaborthreemonthButton.style.backgroundColor = '#117B9E'
            LaborthreemonthButton.style.color = '#fff'
            LaborsixmonthButton.style.backgroundColor = '#fff'
            LaborsixmonthButton.style.color = '#111111'
            LabortenmonthButton.style.backgroundColor = '#fff'
            LabortenmonthButton.style.color = '#111111'
            LaborthreemonthButton.style.display = 'inline-block';
            LaborthreemonthButton.innerHTML = '近三年';
            LaborsixmonthButton.style.display = 'inline-block';
            LaborsixmonthButton.innerHTML = '近五年';
            LabortenmonthButton.style.display = 'inline-block';
            LabortenmonthButton.innerHTML = '近十年';
            Labornowmonth.style.display = 'none'
            Labornowyear.style.display = 'none';
            Laborthreey.style.display = 'inline-block';
            Laborfivey.style.display = 'none';
            Laborteny.style.display = 'none';
            Laborthreem.style.display = 'none';
            Laborsixm.style.display = 'none';
            Labortenm.style.display = 'none';
        }
    }
    else if (LaborChangeMonthyearButton.innerHTML == '年') {
        if (LaborChangeNowendButton.innerHTML == '現況') {
            LaborMonthyearPic.src = 'assets/勞工關係月.png'
            LaborChangeMonthyearButton.innerHTML = '月';
            LaborthreemonthButton.style.backgroundColor = '#117B9E'
            LaborthreemonthButton.style.color = '#fff'
            LaborsixmonthButton.style.backgroundColor = '#fff'
            LaborsixmonthButton.style.color = '#111111'
            LabortenmonthButton.style.backgroundColor = '#fff'
            LabortenmonthButton.style.color = '#111111'
            LaborthreemonthButton.style.display = 'none';
            LaborsixmonthButton.style.display = 'none';
            LabortenmonthButton.style.display = 'none';
            Labornowmonth.style.display = 'inline-block'
            Labornowyear.style.display = 'none';
            Laborthreey.style.display = 'none';
            Laborfivey.style.display = 'none';
            Laborteny.style.display = 'none';
            Laborthreem.style.display = 'none';
            Laborsixm.style.display = 'none';
            Labortenm.style.display = 'none';
        } else if (LaborChangeNowendButton.innerHTML == '歷史') {
            LaborMonthyearPic.src = 'assets/勞工關係月.png'
            LaborChangeMonthyearButton.innerHTML = '月';
            LaborthreemonthButton.style.backgroundColor = '#117B9E'
            LaborthreemonthButton.style.color = '#fff'
            LaborsixmonthButton.style.backgroundColor = '#fff'
            LaborsixmonthButton.style.color = '#111111'
            LabortenmonthButton.style.backgroundColor = '#fff'
            LabortenmonthButton.style.color = '#111111'
            LaborthreemonthButton.style.display = 'inline-block';
            LaborthreemonthButton.innerHTML = '近三月';
            LaborsixmonthButton.style.display = 'inline-block';
            LaborsixmonthButton.innerHTML = '近六月';
            LabortenmonthButton.style.display = 'inline-block';
            LabortenmonthButton.innerHTML = '近十月';
            Labornowmonth.style.display = 'none'
            Labornowyear.style.display = 'none';
            Laborthreey.style.display = 'none';
            Laborfivey.style.display = 'none';
            Laborteny.style.display = 'none';
            Laborthreem.style.display = 'inline-block';
            Laborsixm.style.display = 'none';
            Labortenm.style.display = 'none';
        }
    }
}
// 勞工關係三個月/年按鈕
function LaborThreeMonthButtonfunction() {
    if (LaborChangeNowendButton.innerHTML == '歷史' && LaborChangeMonthyearButton.innerHTML == '月') {
        LaborthreemonthButton.style.backgroundColor = '#117B9E'
        LaborthreemonthButton.style.color = '#fff'
        LaborsixmonthButton.style.backgroundColor = '#fff'
        LaborsixmonthButton.style.color = '#111111'
        LabortenmonthButton.style.backgroundColor = '#fff'
        LabortenmonthButton.style.color = '#111111'
        Labornowmonth.style.display = 'none'
        Labornowyear.style.display = 'none';
        Laborthreey.style.display = 'none';
        Laborfivey.style.display = 'none';
        Laborteny.style.display = 'none';
        Laborthreem.style.display = 'inline-block';
        Laborsixm.style.display = 'none';
        Labortenm.style.display = 'none';
    } else if (LaborChangeNowendButton.innerHTML == '歷史' && LaborChangeMonthyearButton.innerHTML == '年') {
        LaborthreemonthButton.style.backgroundColor = '#117B9E'
        LaborthreemonthButton.style.color = '#fff'
        LaborsixmonthButton.style.backgroundColor = '#fff'
        LaborsixmonthButton.style.color = '#111111'
        LabortenmonthButton.style.backgroundColor = '#fff'
        LabortenmonthButton.style.color = '#111111'
        Labornowmonth.style.display = 'none'
        Labornowyear.style.display = 'none';
        Laborthreey.style.display = 'inline-block';
        Laborfivey.style.display = 'none';
        Laborteny.style.display = 'none';
        Laborthreem.style.display = 'none';
        Laborsixm.style.display = 'none';
        Labortenm.style.display = 'none';
    }
}
// 勞工關係六個月/五年按鈕
function LaborSixMonthButtonfunction() {
    if (LaborChangeNowendButton.innerHTML == '歷史' && LaborChangeMonthyearButton.innerHTML == '月') {
        LaborthreemonthButton.style.backgroundColor = '#fff'
        LaborthreemonthButton.style.color = '#111111'
        LaborsixmonthButton.style.backgroundColor = '#117B9E'
        LaborsixmonthButton.style.color = '#fff'
        LabortenmonthButton.style.backgroundColor = '#fff'
        LabortenmonthButton.style.color = '#111111'
        Labornowmonth.style.display = 'none'
        Labornowyear.style.display = 'none';
        Laborthreey.style.display = 'none';
        Laborfivey.style.display = 'none';
        Laborteny.style.display = 'none';
        Laborthreem.style.display = 'none';
        Laborsixm.style.display = 'inline-block';
        Labortenm.style.display = 'none';
    } else if (LaborChangeNowendButton.innerHTML == '歷史' && LaborChangeMonthyearButton.innerHTML == '年') {
        LaborthreemonthButton.style.backgroundColor = '#fff'
        LaborthreemonthButton.style.color = '#111111'
        LaborsixmonthButton.style.backgroundColor = '#117B9E'
        LaborsixmonthButton.style.color = '#fff'
        LabortenmonthButton.style.backgroundColor = '#fff'
        LabortenmonthButton.style.color = '#111111'
        Labornowmonth.style.display = 'none'
        Labornowyear.style.display = 'none';
        Laborthreey.style.display = 'none';
        Laborfivey.style.display = 'inline-block';
        Laborteny.style.display = 'none';
        Laborthreem.style.display = 'none';
        Laborsixm.style.display = 'none';
        Labortenm.style.display = 'none';
    }
}
// 勞工關係十個月/年按鈕
function LaborTenMonthButtonfunction() {
    if (LaborChangeNowendButton.innerHTML == '歷史' && LaborChangeMonthyearButton.innerHTML == '月') {
        LaborthreemonthButton.style.backgroundColor = '#fff'
        LaborthreemonthButton.style.color = '#111111'
        LaborsixmonthButton.style.backgroundColor = '#fff'
        LaborsixmonthButton.style.color = '#111111'
        LabortenmonthButton.style.backgroundColor = '#117B9E'
        LabortenmonthButton.style.color = '#fff'
        Labornowmonth.style.display = 'none'
        Labornowyear.style.display = 'none';
        Laborthreey.style.display = 'none';
        Laborfivey.style.display = 'none';
        Laborteny.style.display = 'none';
        Laborthreem.style.display = 'none';
        Laborsixm.style.display = 'none';
        Labortenm.style.display = 'inline-block';
    } else if (LaborChangeNowendButton.innerHTML == '歷史' && LaborChangeMonthyearButton.innerHTML == '年') {
        LaborthreemonthButton.style.backgroundColor = '#fff'
        LaborthreemonthButton.style.color = '#111111'
        LaborsixmonthButton.style.backgroundColor = '#fff'
        LaborsixmonthButton.style.color = '#111111'
        LabortenmonthButton.style.backgroundColor = '#117B9E'
        LabortenmonthButton.style.color = '#fff'
        Labornowmonth.style.display = 'none'
        Labornowyear.style.display = 'none';
        Laborthreey.style.display = 'none';
        Laborfivey.style.display = 'none';
        Laborteny.style.display = 'inline-block';
        Laborthreem.style.display = 'none';
        Laborsixm.style.display = 'none';
        Labortenm.style.display = 'none';
    }
}
