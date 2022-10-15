import { Pipe, PipeTransform } from '@angular/core';


@Pipe({ name: 'listPipe' })

export class ListPipe implements PipeTransform {
  transform(val: string, list: any) {
    for (const i in list) {
      if (list[i].key == val) {
        return list[i].label;
      }
    }
    return 'not found';
  }
}
