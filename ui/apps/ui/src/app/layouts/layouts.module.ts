import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MainHeaderComponent } from './main-header.component';
import { LibraryComponent } from './library.component';
import { NzDrawerModule } from 'ng-zorro-antd/drawer';
import { ComponentsModule } from '../components/components.module';
import { NzButtonModule } from 'ng-zorro-antd/button';
import { GridComponent } from './grid.component';
import { GridsterModule } from 'angular-gridster2';
import { NzDropDownModule } from 'ng-zorro-antd/dropdown';
import { WidgetContentComponent } from './widget-content.component';
import { FeedsComponent } from './feeds.component';

@NgModule({
  declarations: [
    MainHeaderComponent,
    LibraryComponent,
    GridComponent,
    WidgetContentComponent,
    FeedsComponent,
  ],
  imports: [
    CommonModule,
    NzDrawerModule,
    ComponentsModule,
    NzButtonModule,
    GridsterModule,
    NzDropDownModule,
  ],
  exports: [MainHeaderComponent, LibraryComponent, GridComponent],
})
export class LayoutsModule {}
