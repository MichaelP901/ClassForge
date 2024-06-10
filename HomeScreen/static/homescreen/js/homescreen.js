document.addEventListener("DOMContentLoaded", function() 
{
    let nav = 0;
  
    const calender = document.getElementById('calender');
    const weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

    function load() {
        const dt = new Date();

        if (nav !== 0) 
        {
            dt.setMonth(new Date().getMonth() + nav);
        }

        const day = dt.getDate();
        const month = dt.getMonth();
        const year = dt.getFullYear();

        const firstDayOfMonth = new Date(year, month, 1);
        const daysInMonth = new Date(year, month + 1, 0).getDate();
        
        const dateString = firstDayOfMonth.toLocaleDateString('en-us', {
            weekday: 'long',
            year: 'numeric',
            month: 'numeric',
            day: 'numeric',
        });

        const paddingDays = weekdays.indexOf(dateString.split(', ')[0]);

        document.getElementById('monthDisplay').innerText =  `${dt.toLocaleDateString('en-us', { month: 'long' })} ${year}`;

        calender.innerHTML = "";

        for(let i = 1; i <= paddingDays + daysInMonth; i++) 
        {
            const daySquare = document.createElement('div');
            daySquare.classList.add('day');

            const dayString = `${month + 1}/${i - paddingDays}/${year}`;

            if (i > paddingDays) 
            {
                daySquare.innerText = i - paddingDays;

                if (i - paddingDays === day && nav === 0) 
                {
                    daySquare.id = 'currentDay';
                }

                if (i <= day + paddingDays - 1)
                {
                    daySquare.style.backgroundColor = "grey";
                }
            }
            else 
            {
                daySquare.classList.add('padding');
            }
        
            if (nav < 0)
            {
                daySquare.style.backgroundColor = "grey";
            }
            
            calender.appendChild(daySquare);    
        }
    }
    
    load();

    
});