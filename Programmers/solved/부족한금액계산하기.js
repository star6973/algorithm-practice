function solution(price, money, count) {
    let answer = 0;
    let tryPrice = 0;
    
    for (let i=1; i<=count; i++) {
        tryPrice = price * i;
        answer += tryPrice;
    }

    return (answer - money >= 0) ? answer - money : 0;
}