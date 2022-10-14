import { TestBed } from '@angular/core/testing';

import { AriregisterApiInterceptor } from './ariregister-api.interceptor';

describe('AriregisterApiInterceptor', () => {
  beforeEach(() => TestBed.configureTestingModule({
    providers: [
      AriregisterApiInterceptor
      ]
  }));

  it('should be created', () => {
    const interceptor: AriregisterApiInterceptor = TestBed.inject(AriregisterApiInterceptor);
    expect(interceptor).toBeTruthy();
  });
});
