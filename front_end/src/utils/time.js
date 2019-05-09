const mouthDict = {
    1: 'Jan',
    2: 'Feb',
    3: 'Mar',
    4: 'Apr',
    5: 'May',
    6: 'Jun',
    7: 'Jul',
    8: 'Aug',
    9: 'Sep',
    10: 'Oct',
    11: 'Nov',
    12: 'Dec',
};

export default {
    monthFromNumber(number) {
        return mouthDict[number]
    },

    getTimeString(timeString) {
        let date = new Date(timeString);
        let year = date.getFullYear().toString();
        let month = (date.getMonth() + 1).toString();
        if (month.length < 2) {
            month = '0' + month;
        }
        let day = date.getDate().toString();
        if (day.length < 2) {
            day = '0' + day;
        }
        let hour = date.getHours().toString();
        let minute = date.getMinutes().toString();
        if (minute.length < 2) {
            minute = '0' + minute;
        }
        return `${year} - ${month} - ${day} ${hour}:${minute}`;
    },
};
