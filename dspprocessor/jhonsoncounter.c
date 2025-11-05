#include <dsk6713,h>
#include<dsk6713_led.h>
#include<dsk6713_dip.h>

voidmain(){
    DSK6713_init();
    DSK6713_LED_init();
    DSK6713_DIP_init();
    while(1){
        if (DSK6713_DIP_get(2)==0){
            int i;
            for(i=0;i<4;i++){
                DSK6713_LED_off(i);
                DSK6713_waitusec(200000);
            }
        }
        else{
            int i;
            for(i=0;i<4;i++){
                DSK6713_LED_on(i);
                DSK6713_waitusec(200000);
            }
            for (i=0;i<4;i++){
                DSK6713_LED_off(i);
                DSK6713_waitusec(200000);
            }
        }
    }
}